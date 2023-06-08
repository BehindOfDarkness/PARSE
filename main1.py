import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("http://httpbin.org/")
browser.follow_link("forms")
browser.select_form('form[action="/post"]')
print(browser.form.print_summary())

browser["custname"] = "Best Customer"
browser["custtel"] = "+7 951 123 45 67"
browser["custemail"] = "pex@example.com"
browser["size"] = "large"
browser["topping"] = ("cheese", "mushroom")
browser["comments"] = "Add more anything, please."

response = browser.submit_selected()

print(response.text)
