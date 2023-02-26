# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class nba(models.Model):
#     _name = 'nba.nba'
#     _description = 'nba.nba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class equipo(models.Model):
	_name = 'nba.equipo'
	_description = 'model equipo'

	name = fields.Char('Codigo equipo', required = True)
	nombre = fields.Char(string='Nombre', required = True)
	ciudad = fields.Char(string='Ciudad', required = True)
	division = fields.Char(string='Division', required = True)

class jugador(models.Model):
	_name = 'nba.jugador'
	_description = 'model jugador'

	name = fields.Char('Codigo jugador', required = True)
	nombre = fields.Char(string='Nombre', required = True)
	numero = fields.Integer(string='Numero', required = True)
	equipo_id = fields.Many2one('nba.equipo',string='Equipo')

class partido(models.Model):
	_name = 'nba.partido'
	_description = 'model partido'

	name = fields.Char('Codigo partido', required = True)
	equipoLocal_id = fields.Many2one('nba.equipo', string='Equipo local')
	equipoVisitante_id = fields.Many2one('nba.equipo',string='Equipo visitante')
	resultado = fields.Char(string='Resultado', required = True)

	