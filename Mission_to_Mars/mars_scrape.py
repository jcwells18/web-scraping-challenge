{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.5 64-bit (conda)",
   "metadata": {
    "interpreter": {
     "hash": "320b063615c881cf99d5bda0a05a87a093cceae5b3aed84278fa7ef3d4b95f2a"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import necessary libraries\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd \n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 89.0.4389\n",
      "[WDM] - Get LATEST driver version for 89.0.4389\n",
      "[WDM] - Driver [C:\\Users\\Julie\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe] found in cache\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#create browser instance\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path,headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#go to Mars News url page\n",
    "marsnews_url = 'https://mars.nasa.gov/news'\n",
    "browser.visit(marsnews_url)\n",
    "\n",
    "#create beautiful soup object\n",
    "html = browser.html\n",
    "marsnews_soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "The title is:\nNASA Ingenuity Mars Helicopter Prepares for First Flight\n\nThe paragraph is: \nNow uncocooned from its protective carbon-fiber shield, the helicopter is being readied for its next steps.  \n"
     ]
    }
   ],
   "source": [
    "#find news titles\n",
    "article = marsnews_soup.find(\"div\",class_='list_text')\n",
    "\n",
    "news_title = article.find(\"div\",class_=\"content_title\").text\n",
    "\n",
    "#find paragraph\n",
    "news_p = article.find(\"div\",class_=\"article_teaser_body\").text\n",
    "\n",
    "#close browser\n",
    "print(f\"The title is:\\n{news_title}\")\n",
    "print()\n",
    "print(f\"The paragraph is: \\n{news_p}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.htmlimage/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "#url for JPL Featured Space Image\n",
    "\n",
    "jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'\n",
    "\n",
    "browser.visit(jpl_url)\n",
    "\n",
    "#create soup item\n",
    "image_html = browser.html\n",
    "image_soup = BeautifulSoup(image_html,'html.parser')\n",
    "\n",
    "image_url = image_soup.find('img',class_=\"headerimage fade-in\")['src']\n",
    "\n",
    "\n",
    "featured_image_url = jpl_url+image_url\n",
    "\n",
    "print(featured_image_url)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 ?? 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 ??C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 ?? 10^23 kg  5.97 ?? 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 ??C      -88 to 58??C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 ?? 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 ??C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "metadata": {},
     "execution_count": 33
    }
   ],
   "source": [
    "#spacefacts url\n",
    "url = 'https://space-facts.com/mars/'\n",
    "\n",
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 ?? 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 ??C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Description</th>\n      <th>Value</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Mass:</td>\n      <td>6.39 ?? 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 ??C</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 35
    }
   ],
   "source": [
    "#create facts dataframe\n",
    "facts_df = tables[0]\n",
    "facts_df.columns =['Description','Value']\n",
    "facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert to html\n",
    "facts_df.to_html('marsfacts.html',index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#astreogeologoy url\n",
    "base_url = \"https://astrogeology.usgs.gov\"\n",
    "mars_hem_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "browser.visit(mars_hem_url)\n",
    "\n",
    "#create list \n",
    "hemisphere_image_urls = []\n",
    "\n",
    "#create html object\n",
    "html = browser.html\n",
    "\n",
    "#create beautiful soup object\n",
    "soup = BeautifulSoup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "-\n",
      "Cerberus Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n",
      "-\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n",
      "-\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n",
      "-\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "#grab all divs\n",
    "hem_divs = soup.find_all('div',class_='item')\n",
    "\n",
    "#loop through items\n",
    "for item in hem_divs:\n",
    "\n",
    "    #find title\n",
    "    hem = item.find('div',class_='description')\n",
    "    title = hem.h3.text\n",
    "\n",
    "    #set base url\n",
    "    base_url = \"https://astrogeology.usgs.gov\"\n",
    "    hem_url = hem.a['href']\n",
    "    browser.visit(base_url+hem_url)\n",
    "\n",
    "    #create html and beautiful soup item\n",
    "    img_html = browser.html\n",
    "    img_soup = BeautifulSoup(img_html,'html.parser')\n",
    "\n",
    "    #find image url\n",
    "    img_src = img_soup.find('li').a['href']\n",
    "    #print results\n",
    "    if (title and img_src):\n",
    "        #print\n",
    "        print(\"-\")\n",
    "        print(title)\n",
    "        print(img_src)\n",
    "\n",
    "        #dictionary for title and url\n",
    "        hem_data = {'title':title, 'image_url': img_src}\n",
    "\n",
    "        #append to list\n",
    "        hemisphere_data.append(hem_data)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}