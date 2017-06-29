# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo import tools
from odoo.tools.translate import _

class IICAContactsController(http.Controller):
    @http.route('/contact/register', type='http', auth='public', website='true')
    def register(self, redirect=None, **post):

        areas_interest = request.env['iica_contacts.area_interest'].sudo().search([])
        topics_interest = request.env['iica_contacts.topic_interest'].sudo().search([])
        products_interest = request.env['iica_contacts.products_interest'].sudo().search([])
        countries = request.env['res.country'].sudo().search([])

        values = {
            'areas_interest' : areas_interest,
            'topics_interest' : topics_interest,
            'products_interest' : products_interest,
            'countries' : countries,
        }

        if post:
            error_message, valid = self._validate_form(post)
            if valid == 1:
                self._process_registration(post)
                return request.redirect('/contact/register/success')
            else:
                return request.redirect('/contact/register/error')
        else:
            contact = request.env['iica_contacts.contact']
            values.update({
                'contact' : contact,
            })

        return request.render("iica_contacts.register", values)

    @http.route('/contact/register/success', type='http', auth='public', website='true')
    def register_success(self, **kw):
        return request.render("register_confirmation")

    @http.route('/contact/register/error', type='http', auth='public', website='true')
    def register_success(self, **kw):
        return request.render("register_error")

    #Métodos privados
    def _process_registration(self, post):
        request.env['iica_contacts.contact'].create({
            'name' : post.get('name'),
            'company' : post.get('company'),
            'country_id': post.get('country_id'),
            'sector' : post.get('sector'),
            'language' : post.get('language'),
            'email' : post.get('email'),
            'phone' : post.get('phone'),
            'area_interest_ids' : self._process_many2may(request.httprequest.form.getlist('areas_interest')),
            'product_interest_ids' : self._process_many2may(request.httprequest.form.getlist('products_interest')),
            'topic_interest_ids' : self._process_many2may(request.httprequest.form.getlist('topics_interest')),
        })

    def _validate_form(self, post):
        error_message = []
        valid = 1

        if not post.get('name'):
            error_message.append(_("You must type your name to continue. "))
            valid = 0

        if not post.get('email'):
            error_message.append(_("The email is a required field."))
            valid = 0
        else:
            if not tools.single_email_re.match(post.get('email')):
                error_message.append(_('Invalid email! Please enter a valid email address.'))
                valid = 0

        return error_message, valid



    def _process_many2may(self, values):
        retValue = []
        for v in values:
            retValue.append((4, int(v)))
        return retValue
