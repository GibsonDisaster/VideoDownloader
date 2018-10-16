import urllib2
import wget
from bs4 import BeautifulSoup

def isVideo(h):
    fileType = h[-3:]
    return (fileType == "mp4")

def download_vid(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()
    for anchor in soup.findAll('a', href=True):
        if isVideo(anchor['href']):
            print(anchor['href'])
            #wget.download(anchor['href'])

def getShowsFromSideBar():
    shows = []
    page = urllib2.urlopen("https://my.viebit.com/").read()
    soup = BeautifulSoup(page, "html.parser")
    for contfluid in soup.find_all('div', {'class' : 'container-fluid vbContent'}):
        for col_md in contfluid.find_all('div', {'class' : 'col-md-2'}):
            for sticky_wrapper in col_md.find_all('div'):
                for showNames in sticky_wrapper.find_all('a', {'class' : 'top_folder'}):
                    shows.append(showNames.contents[1])
    return shows

def download_show_page(page):
    ep_links = []
    soup = BeautifulSoup(open("/home/henningtonko/Desktop/Python/WadsworthArchive/pages/" + page), "html.parser")
    for contfluid in soup.find_all('div', {'class' : 'container-fluid vbContent'}):
         for row in contfluid.find_all('div', {'class' : 'row'}):
             for col_mid in row.find_all('div', {'class' : 'col-md-6'}):
                 for vbVODSel in col_mid.find_all('div', {'class' : 'vbVODSel'}):
                     for panel_panel_def in vbVODSel.find_all('div', {'class' : 'panel panel-default vodFolder'}):
                         for panel_body in panel_panel_def.find_all('div', {'class' : 'panel-body'}):
                             for contf in panel_body.find_all('div', {'class' : 'container-fluid'}):
                                 for gridVODS in contf.find_all('div', {'id' : 'gridVOD'}):
                                     for l in gridVODS.find_all('div', {'class' : 'vbPoster'}):
                                         for link_anchors in l.find_all('a'):
                                             ep_links.append(link_anchors['href'])
    for x in ep_links:
        download_vid(x)

def main():
    getShowsFromSideBar()
    #download_show_page("./pages/test.html")

if __name__ == "__main__":
    main()
