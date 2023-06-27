from googlesearch import search


def search_links(response):
    links = []
    response = response.split("\n")
    for i in range(len(response)):
        response[i] = response[i][3:]
    for i in response:
        query = next(search(i, tld="com", num=1, stop=1, pause=2.0), None)
        links.append(query)
    return links


response = """1) learn or take a course on programming languages such as Python, Java, or Ruby.
(2) learn or take a course on databases such as MySQL, PostgreSQL, or MongoDB.
(3) learn or take a course on web frameworks such as Django, Flask, or Ruby on Rails."""

print(search_links(response))
# query = "python fastapi"

# for i in search(query, tld='com', num=5, stop=5):
#     print(i)

# a = """1. HTML and CSS fundamentals
# 2. JavaScript basics
# 3. Responsive web design
# 4. CSS preprocessors (Sass, Less)
# 5. JavaScript frameworks (React, Angular, Vue)
# 6. Frontend build tools (Webpack, Gulp)
# 7. Version control with Git
# 8. Testing frameworks (Jest, Enzyme)
# 9. Progressive Web Apps (PWA)
# 10. Server-side rendering (SSR)
# 11. Accessibility (a11y) and web standards
# 12. Performance optimization
# 13. Web security and best practices
# 14. Continuous integration and deployment (CI/CD)
# 15. Advanced topics (Web components, GraphQL, WebAssembly)"""


# links = ['https://www.codecademy.com/catalog/language/html-css',
#          'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics',
#          'https://www.w3schools.com/html/html_responsive.asp',
#          'https://www.keycdn.com/blog/sass-vs-less',
#          'https://www.browserstack.com/guide/angular-vs-react-vs-vue',
#          'https://www.goodcore.co.uk/blog/webpack-vs-gulp/',
#          'https://commons.wikimedia.org/wiki/File:Git-logo.svg',
#          'https://medium.com/codeclan/testing-react-with-jest-and-enzyme-20505fec4675',
#          'https://en.wikipedia.org/wiki/Progressive_web_app',
#          'https://www.heavy.ai/technical-glossary/server-side-rendering',
#          'https://developer.mozilla.org/en-US/docs/Web/Accessibility',
#          'https://www.cloverinfotech.com/blog/what-is-performance-tuning-how-it-affects-corporations/',
#          'https://www.acunetix.com/blog/web-security-zone/7-web-application-security-best-practices/',
#          'https://www.novelvista.com/blogs/devops/what-is-continuous-deployment-delivery',
#          'https://github.com/nepaul/awesome-web-development']


# print(links)
