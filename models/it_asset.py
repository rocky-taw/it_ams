from odoo import api, fields, models


class ITAsset(models.Model):
    _name = "it.asset"
    _description = "IT Asset New"

    name = fields.Many2one('hr.employee', string='Name', required=True)
    department_id = fields.Many2one('hr.department', string='Department')
    job_id = fields.Many2one('hr.job', string='Job Title')

    device = fields.Selection(
        [('desktop', "Desktop"),
         ('laptop', "Laptop")],
        string='Device', required=True,
        default='desktop')

    asset_property = fields.Selection(
        [('personal', "Personal"),
         ('company', "Company")],
        string='Device Property', required=True,
        default='company')

    work_email = fields.Char('Email', size=240)
    mobile_phone = fields.Char('Mobile', readonly=False)
    work_location = fields.Char('Office Location')
    ip_address = fields.Char('IP Address')
    subnet_masks = fields.Char('Subnet Mask')
    gateway = fields.Char('Gateway')
    hr_name = fields.Char(' Name')
    hr_department = fields.Char(' Department')
    hr_designation = fields.Char(' Designation')
    admin_name = fields.Char(' Name')
    admin_department = fields.Char(' Department')
    admin_designation = fields.Char(' Designation')

    note = fields.Text('Note')

    asset_line_ids = fields.One2many('it.asset.line', 'it_asset_id', 'Assets Details', required=True)

    @api.onchange('name')
    def _onchange_employee_id(self):
        if self.name:
            self.department_id = self.name.department_id and self.name.department_id.id or False
            self.job_id = self.name.job_id
            self.work_email = self.name.work_email
            self.mobile_phone = self.name.mobile_phone
            self.work_location = self.name.work_location


class ITAssetLine(models.Model):
    _name = 'it.asset.line'
    _description = "Asset Details"

    it_asset_id = fields.Many2one('it.asset', string='Order')
    product_id = fields.Many2one('product.product', string='Product', domain=[('isAsset', '=', True)])
    details = fields.Char('Details')
    receive_date = fields.Date('Receive Date', required=True)
    return_date = fields.Date('Return Date')
    model_name = fields.Char('Model')
    brand_name = fields.Char('Brand')
    vendor_name = fields.Char('Vendor')
