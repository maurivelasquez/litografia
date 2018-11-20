# -*- coding: utf-8 -*-
# Copyright 2018 Mauricio Restrepo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api

Class PaperType(models.Model):
    _name='label.paper'
    name=fields.Char(string='Nombre')
    cost=fields.float(string='Costo($/m2)')

Class Printer(models.Model):
    _name='label.printer'
    name=fields.Char(string='Nombre')
    roller_width=fields.float(string='Ancho del rodillo(Pulgadas)')
    set_time=fields.Float('Tiempo de preparación(Horas)')
    speed=fields.Float('Velocidad impresión(Pulgadas/min)')
    type=fields.Selection([('digital','Digital'),('flexografica','Flexográfica')])    

class PrintConfig(models.Model):
    _name='print.config'
    inks_qty=fields.Integer(string='Número de tintas',required=True)
    label_width=fields.Float(string='Ancho(mm)')
    label_height=fields.Float(string='Largo(mm)')
    label_area=fields.Float(compute='compute_area')
    label_waste=fields.Float('Desperdicio de papel(%)')
    printer_id=fields.Many2one('label.printer', string='Impresora')
    paper_id=fields.Many2one('label.paper', string='Papel')
    
    @api.onchange('label_width','label_height') 
    def area(self):
        a=self.label_width*self.label_height
        self.area= a
        
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    print_config_id=fields.Many2one('print.config',string='Conf Impresión')
    
    
