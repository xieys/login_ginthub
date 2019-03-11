# -*- coding: utf-8 -*-
"""
针对form表单的action属性有明确的url
"""
import scrapy


class LoginGithub2Spider(scrapy.Spider):
    name = 'login_github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'login': 'username', 'password': 'password'},
            callback=self.after_login
        )

    def after_login(self, response):
        project_list = response.xpath('//ul[@data-filterable-for="dashboard-repos-filter-left"]/li')
        for i in project_list:
            project = i.extract()
            print(project)
