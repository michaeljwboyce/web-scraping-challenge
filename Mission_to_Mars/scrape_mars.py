def scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    title = soup.find("div",class_="bottom_gradient").text
    blurb = soup.find("div", class_="article_teaser_body").text
    
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    pic = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://jpl.nasa.gov"+pic

    twt_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twt_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tweets = soup.find_all('span')
    for tweet in tweets:
    print(tweet.text)