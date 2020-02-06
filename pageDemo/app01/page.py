#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Pagination(object):
    def __init__(self,current_page,all_count,request,per_page=10,max_pager_num=11):
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page =1

        if current_page < 1:
            current_page = 1
        self.current_page = current_page
        self.all_count = all_count
        self.per_page = per_page

        #总页数
        all_pager,tmp = divmod(all_count,per_page)
        if tmp:
            all_pager += 1
        self.all_pager = all_pager
        self.max_pager_num =  max_pager_num

        self.pager_count_half = int((self.max_pager_num -1)/2)

        #请求信息字典
        import copy
        self.params = copy.deepcopy(request.GET)
        # self.params.pop("page")
        # ["page"] = self.pager_count_half

        print("::::",self.params)




    @property
    def start(self):
        return (self.current_page-1) * self.per_page

    @property
    def end(self):
        return (self.current_page) * self.per_page

    def page_html(self):
        #如果总页码数小于11个
        if self.all_pager < self.max_pager_num:
            pager_start =1
            pager_end =self.all_pager + 1

        #总页码 > 11
        else:
            #当前页如果<=页面上最多显示11/2个页码
            if self.current_page <= self.pager_count_half:
                pager_start = 1
                pager_end =self.max_pager_num + 1
            else:
                #如果页码没有右5的情况
                if self.current_page + self.pager_count_half >= self.all_pager:
                    pager_start= self.all_pager - self.max_pager_num + 1
                    pager_end = self.all_pager + 1
                else:
                    pager_start = self.current_page - self.pager_count_half
                    pager_end = self.current_page + self.pager_count_half +1
        print(">>>>",pager_start,pager_end)
        page_html_list = []

        self.params["page"] = 1
        first_page = '<nav aria-label="Page navigation"><ul class="pagination"><li><a href="?%s">首页</a></li>'%(self.params.urlencode(),)
        page_html_list.append(first_page)


        if self.current_page <= 1:
            prev_page = '<li class="disable"><a>上一页</a></li>'
        else:
            self.params["page"] = self.current_page - 1
            prev_page = '<li><a href="?%s">上一页</a></li>'%(self.params.urlencode(),)
        page_html_list.append(prev_page)



        for i in range(pager_start,pager_end):
            self.params["page"] = i
            if i == self.current_page:
                temp = '<li class="active"><a href="?%s"">%s</a></li>'%(self.params.urlencode(),i)
            else:
                temp = '<li><a href="?%s">%s</a></li>'%(self.params.urlencode(),i)
            # print(temp)
            page_html_list.append(temp)



        if self.current_page < self.all_pager:
            self.params["page"] = self.current_page + 1
            second_page = '<li><a href="?%s">下一页</a></li>'%self.params.urlencode()
        else:
            second_page = '<li class="disable"><a>下一页</a></li>'

        page_html_list.append(second_page)

        self.params["page"] = self.all_pager
        last_page = '<li><a href="?%s">末页</a></li></ul></nav>'%self.params.urlencode()
        page_html_list.append(last_page)

        return ''.join(page_html_list)

