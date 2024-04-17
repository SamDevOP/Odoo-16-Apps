from odoo.exceptions import MissingError, UserError, ValidationError
from odoo import api, fields, models, tools, _
import logging
_logger = logging.getLogger(__name__)

class inheritPOSorder(models.Model):
    _inherit ='pos.order'
    
    def get_order_details(self):
        """
        <tree string="Order lines" editable="bottom">
            <field name="full_product_name"/>
            <field name="pack_lot_ids" widget="many2many_tags" groups="stock.group_production_lot"/>
            <field name="qty"/>
            <field name="customer_note" optional="hide"/>
            <field name="product_uom_id" string="UoM" groups="uom.group_uom"/>
            <field name="price_unit" widget="monetary"/>
            <field name="is_total_cost_computed" invisible="1"/>
            <field name="total_cost" attrs="{'invisible': [('is_total_cost_computed','=', False)]}" optional="hide" widget="monetary"/>
            <field name="margin" attrs="{'invisible': [('is_total_cost_computed','=', False)]}" optional="hide" widget="monetary"/>
            <field name="margin_percent" attrs="{'invisible': [('is_total_cost_computed','=', False)]}" optional="hide" widget="percentage"/>
            <field name="discount" string="Disc.%"/>
            <field name="tax_ids_after_fiscal_position" widget="many2many_tags" string="Taxes"/>
            <field name="tax_ids" widget="many2many_tags" invisible="1"/>
            <field name="price_subtotal" widget="monetary" force_save="1"/>
            <field name="price_subtotal_incl" widget="monetary" force_save="1"/>
            <field name="currency_id" invisible="1"/>
            <field name="refunded_qty" optional="hide"/>
        </tree>
        """
        receipt_data ={}
        receipt_data['items']=[]
        for recs in self.lines:
            items = {
                
                'full_product_name':recs.full_product_name,
                'qty':recs.qty,
                'product_uom_id':recs.product_uom_id,
                'price_unit':recs.price_unit,
                'price_subtotal':recs.price_subtotal,
           
            }
            receipt_data['items'].append(items)
            
        receipt_data.update({
            'order_name': self.name,
            'amount_tax':self.amount_tax,
            'amount_total': self.amount_total,
            'amount_paid':self.amount_paid
        })
        _logger.error(receipt_data)
        return receipt_data

            
        