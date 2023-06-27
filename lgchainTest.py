from langchain.llms import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

llm = OpenAI(temperature=0)


def search_links_lch(response):
    links = []
    response = response.split("\n")
    for i in response:
        query = llm.predict(f"give 1 link of resource for each topic to learn {i}")
        links.append(query)
    return links


# response = """(1) Learn and take a course on programming languages such as Python, Java, or Ruby.
# (2) Learn and take a course on databases such as MySQL, PostgreSQL, or MongoDB.
# (3) Learn and take a course on web frameworks such as Django, Flask, or Ruby on Rails.
# (4) Learn and take a course on version control systems such as Git.
# (5) Learn and take a course on server management and deployment using tools such as Docker, Kubernetes, or AWS.
# (6) Learn and take a course on testing frameworks such as Pytest or JUnit.
# (7) Learn and take a course on security best practices for web applications.
# (8) Learn and take a course on API design and development using REST or GraphQL.
# (9) Learn and take a course on performance optimization techniques for web applications.
# (10) Learn and take a course on software architecture and design patterns."""

# # print(search_links_lch(response))
# a = ['\n\nPython: https://www.codecademy.com/learn/learn-python\nJava: https://www.udemy.com/course/java-tutorial/\nRuby: https://www.codecademy.com/learn/learn-ruby', '\n\nMySQL: https://www.mysqltutorial.org/\n\nPostgreSQL: https://www.postgresqltutorial.com/\n\nMongoDB: https://university.mongodb.com/', '\n\n1. Django: https://www.djangoproject.com/start/\n2. Flask: https://flask.palletsprojects.com/en/1.1.x/tutorial/\n3. Ruby on Rails: https://guides.rubyonrails.org/getting_started.html', '\n\n1. Introduction to Version Control with Git: https://www.edx.org/course/introduction-version-control-git-linuxfoundationx-lfs101x-0\n2. Learn Git: https://www.codecademy.com/learn/learn-git\n3. Version Control with Git: https://www.udacity.com/course/version-control-with-git--ud123\n4. Git and GitHub for Beginners: https://www.udemy.com/course/git-and-github-for-beginners/', '\n\n1. Docker: https://training.docker.com/category/docker-certification\n2. Kubernetes: https://www.edx.org/course/introduction-to-kubernetes\n3. AWS: https://aws.amazon.com/training/\n4. Server Management: https://www.udemy.com/course/server-management-and-deployment/\n5. Deployment: https://www.udemy.com/course/deployment-with-docker-kubernetes-aws/', '\n\n1. Pytest: https://www.udemy.com/course/pytest-tutorial-for-beginners/\n2. JUnit: https://www.udemy.com/course/junit-tutorial-for-beginners/\n3. Machine Learning: https://www.udemy.com/course/machinelearning/\n4. Data Science: https://www.udemy.com/course/data-science-and-machine-learning-with-python/\n5. Python Programming: https://www.udemy.com/course/complete-python-bootcamp/\n6. Web Development: https://www.udemy.com/course/the-complete-web-development-bootcamp/', '\n\n1. Security Best Practices for Web Applications: https://www.udemy.com/course/security-best-practices-for-web-applications/\n\n2. Learn Python: https://www.codecademy.com/learn/learn-python\n\n3. Learn HTML and CSS: https://www.codecademy.com/learn/learn-html-css\n\n4. Learn JavaScript: https://www.codecademy.com/learn/introduction-to-javascript\n\n5. Learn SQL: https://www.codecademy.com/learn/learn-sql\n\n6. Learn Machine Learning: https://www.coursera.org/learn/machine-learning\n\n7. Learn Data Science: https://www.coursera.org/specializations/data-science', '\n\n1. REST API Design and Development Course: https://www.udemy.com/course/rest-api-design-and-development-with-nodejs/\n2. GraphQL Course: https://www.udemy.com/course/graphql-with-react-hooks-and-apollo/\n3. Learn HTML: https://www.codecademy.com/learn/learn-html\n4. Learn CSS: https://www.codecademy.com/learn/learn-css\n5. Learn JavaScript: https://www.codecademy.com/learn/introduction-to-javascript\n6. Learn React: https://www.codecademy.com/learn/react-101\n7. Learn Node.js: https://www.codecademy.com/learn/introduction-to-nodejs\n8. Learn MongoDB: https://www.codecademy.com/learn/learn-mongodb', '\n\n1. Performance Optimization Techniques for Web Applications: https://www.udemy.com/course/performance-optimization-techniques-for-web-applications/\n\n2. Learn HTML: https://www.codecademy.com/learn/learn-html\n\n3. Learn CSS: https://www.codecademy.com/learn/learn-css\n\n4. Learn JavaScript: https://www.codecademy.com/learn/introduction-to-javascript\n\n5. Learn React: https://www.codecademy.com/learn/react-101\n\n6. Learn Node.js: https://www.codecademy.com/learn/introduction-to-nodejs\n\n7. Learn MongoDB: https://university.mongodb.com/\n\n8. Learn Python: https://www.codecademy.com/learn/learn-python\n\n9. Learn DevOps: https://www.udemy.com/course/devops-fundamentals/', '\n\n1. Software Architecture and Design Patterns: https://www.coursera.org/learn/software-architecture-design-patterns\n2. Machine Learning: https://www.coursera.org/learn/machine-learning\n3. Data Science: https://www.coursera.org/specializations/data-science\n4. Web Development: https://www.codecademy.com/learn/learn-html\n5. Database Management: https://www.coursera.org/learn/database-management\n6. Cloud Computing: https://www.coursera.org/learn/cloud-computing\n7. Artificial Intelligence: https://www.coursera.org/learn/artificial-intelligence\n8. Cyber Security: https://www.coursera.org/learn/cyber-security\n9. DevOps: https://www.edx.org/course/devops-fundamentals\n10. Blockchain: https://www.coursera.org/learn/blockchain-basics']

# print(len(a))
