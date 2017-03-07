# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError

# TODO MAKE TEST
class PartnerMixin(models.AbstractModel):
    _name = 'partner.mixin'
    _description = "Partner Mixin"

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIPS
    # ----------------------------------------------------------
    partner_id = fields.Many2one('res.partner', string="Contact", ondelete='cascade')

    # RELATED FIELDS
    # ----------------------------------------------------------
    is_company = fields.Boolean(related='partner_id.is_company', default=False)
    name = fields.Char(related='partner_id.name')
    image = fields.Binary(related='partner_id.image')
    image_medium = fields.Binary(related='partner_id.image_medium')
    image_small = fields.Binary(related='partner_id.image_small')
    phone = fields.Char(related='partner_id.phone')
    mobile = fields.Char(related='partner_id.mobile')
    email = fields.Char(related='partner_id.email')
    website = fields.Char(related='partner_id.website')
    # Address
    type = fields.Selection(related='partner_id.type', default='contact')
    street = fields.Char(related='partner_id.street')
    street2 = fields.Char(related='partner_id.street2')
    city = fields.Char(related='partner_id.city')
    country_id = fields.Many2one('res.country', related='partner_id.country_id',
                                 default=lambda self: self.env.ref('base.ae'))
    state_id = fields.Many2one("res.country.state", related='partner_id.state_id',
                               string='Emirates', domain="[('country_id','=',country_id)]")
    contact_address = fields.Char(related='partner_id.contact_address')

    # ONCHANGE FIELDS
    # ----------------------------------------------------------

    # CONSTRAINS
    # ----------------------------------------------------------
    @api.constrains('partner_id')
    def _check_one_partner_only(self):
        """
        ensure one to one relationship
        """
        partner_ids = self.search([('partner_id', '=', self.partner_id.id)])
        if len(partner_ids) > 0 and self not in partner_ids:
            raise ValidationError('partner and vendor should be one to one only')

    # POLYMORPH FUNCTIONS
    # ----------------------------------------------------------
    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, values):
        """
        Creates partner object related to this object
        """
        related_fields = ['is_company', 'name', 'image', 'image_medium',
                          'image_small', 'phone', 'mobile', 'email',
                          'type', 'street', 'street2', 'city', 'country_id', 'contact_address']

        # Remove to fix warning log creating with non existing fields
        if not values.get('partner_id'):
            partner_vals = dict()
            for i in related_fields:
                partner_vals[i] = values.pop(i, False)
            partner_id = self.partner_id.create(partner_vals)
            values['partner_id'] = partner_id.id

        return super(PartnerMixin, self).create(values)

    @api.multi
    def unlink(self):
        self.partner_id.unlink()
        return super(PartnerMixin, self).unlink()