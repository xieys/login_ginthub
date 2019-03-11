# -*- coding: utf-8 -*-
import scrapy


class LoginGithubSpider(scrapy.Spider):
    name = 'login_github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        commit = response.xpath('//input[@name="commit"]/@value').extract_first()
        utf8 = response.xpath('//input[@name="utf8"]/@value').extract_first()
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        form_data = dict(
            commit=commit,
            utf8=utf8,
            authenticity_token=authenticity_token,
            login='username',
            password='password'
        )
        print(form_data)
        yield scrapy.FormRequest(
            'https://github.com/session',
            callback=self.after_login,
            formdata=form_data
        )

    def after_login(self, response):
        project_list = response.xpath('//ul[@data-filterable-for="dashboard-repos-filter-left"]/li')
        for i in project_list:
            project = i.extract()
            print(project)
