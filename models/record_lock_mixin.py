# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError


class RecordLockMixin(models.AbstractModel):
    _name = 'record.lock.mixin'
    _description = "Record Lock Mixin"

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIPS
    # ----------------------------------------------------------

    # RELATED FIELDS
    # ----------------------------------------------------------

    # CALCULATED FIELDS
    # ----------------------------------------------------------
    is_record_lock = fields.Boolean(string='Is Record Lock',
                                    compute='_compute_is_record_lock',
                                    store=True,
                                    default=False)

    @api.one
    @api.depends()
    def _compute_is_record_lock(self):
        """
        Must be overwrite with condition and return True if record should be lock and False if not
        """
        self.is_record_lock = False

    @api.one
    def write(self, values):
        if self.is_record_lock and not self.user_has_groups('base.group_system'):
            raise ValidationError('Record is Locked')
        return super(RecordLockMixin, self).write(values)

    @api.multi
    def unlink(self):
        if self.is_record_lock and not self.user_has_groups('base.group_system'):
            raise ValidationError('Record is Locked')
        return super(RecordLockMixin, self).unlink()

        # ----------------------------------------------------------

        # POLYMORPH FUNCTIONS
        # ----------------------------------------------------------
