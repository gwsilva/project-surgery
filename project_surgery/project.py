# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gideoni Silva (Omnes)
#    Copyright 2013-2014 Omnes Tecnologia
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, osv, fields

class project(orm.Model):
    _inherit = "project.project"
    _columns = {
        'doctor_id': fields.many2one(
        'res.partner', 'Doctor',
        domain = "[('is_company','=',False)]",
        required=True,change_default=True, select=True, track_visibility='always'
        ),
        'patient_id': fields.many2one(
        'res.partner', 'Patient',
        domain = "[('is_company','=',False)]",
        required=True,change_default=True, select=True, track_visibility='always'
        ),
        'hospital_id': fields.many2one(
        'res.partner', 'Hospital',
        domain = "[('is_company','=',True)]",
        required=True,change_default=True, select=True, track_visibility='always'),
        'box_ids': fields.many2many(
        'stock.tracking','project_stock_track_rel','project_id','stock_tracking_id',
        string='Used Surgical Boxes ',
        help="Selecione as Caixas Cirúrgicas para a Cirurgia"
        )
        }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
