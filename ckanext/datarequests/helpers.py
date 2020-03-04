# -*- coding: utf-8 -*-

# Copyright (c) 2015 CoNWeT Lab., Universidad Politécnica de Madrid

# This file is part of CKAN Data Requests Extension.

# CKAN Data Requests Extension is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# CKAN Data Requests Extension is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with CKAN Data Requests Extension. If not, see <http://www.gnu.org/licenses/>.

import ckan.model as model
import ckan.plugins.toolkit as tk
import db


def get_comments_number(datarequest_id):
    # DB should be intialized
    db.init_db(model)
    return db.Comment.get_datarequest_comments_number(datarequest_id=datarequest_id)


def get_comments_badge(datarequest_id):
    return tk.render_snippet('datarequests/snippets/badge.html',
                             {'comments_count': get_comments_number(datarequest_id)})


def get_open_datarequests_number():
    # DB should be initialized
    db.init_db(model)
    return db.DataRequest.get_open_datarequests_number()


def get_open_datarequests_badge(show_badge):
    '''The snippet is only returned when show_badge == True'''
    if show_badge:
        return tk.render_snippet('datarequests/snippets/badge.html',
                                 {'comments_count': get_open_datarequests_number()})
    else:
        return ''
def get_available_organizations_all():                                                                                                        
    '''Get the organization lists for every user'''                                                                                           
    context = {'model': model, 'session': model.Session, 'user': tk.c.user}                                                                   
    data_dict = {}                                                                                                                            
    return tk.get_action('organization_list')(context,data_dict)
    #return logic.get_action('organization_show')(context,data_dict)                                                                          
    #return logic.get_action('organization_list_for_user')(context, {'permission':'read'})