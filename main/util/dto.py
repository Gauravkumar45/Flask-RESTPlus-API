# the data transfer object (DTO) will be responsible for carrying data between processes. In our own case, it will be used for marshaling data for our API calls.
from flask_restplus import Namespace, fields

class UsersDto:
    api = Namespace('Users', description='Users related operations')
    users = api.model('Users', {
        'UserId': fields.Integer(required=True, description='UserId'),
        'Username': fields.String(required=True, description='Username'),
        'DisplayName': fields.String(required=True, description='DisplayName'),
        'Email': fields.String(required=True, description='Email'),
        'Source': fields.String(required=True, description='Source'),
        'PasswordHash': fields.String(required=True, description='PasswordHash'),
        'PasswordSalt': fields.String(required=True, description='PasswordSalt'),
        'LastDirectoryUpdate': fields.DateTime(required=True, description='LastDirectoryUpdate'),
        'UserImage': fields.String(required=True, description='UserImage'),
        'InsertDate': fields.DateTime(required=True, description='InsertDate'),
        'InsertUserId': fields.Integer(required=True, description='InsertUserId'),
        'UpdateDate': fields.DateTime(required=True, description='UpdateDate'),
        'UpdateUserId': fields.Integer(required=True, description='UpdateUserId'),
        'IsActive': fields.Integer(required=True, description='IsActive'),
        'Password': fields.String(required=True, description='Password')
    })

class LocationsDto:
    api = Namespace('Locations', description='Locations related operations')
    locations = api.model('Locations', {
        'locationid': fields.Integer(required=True, description='locations Identifier'),
        'location': fields.String(required=True, description='locationname'),
        'locationcode': fields.String(required=True, description='locationcode'),
        'createdate': fields.DateTime(required=True, description='createdate')
    })

class OwnersDto:
    api = Namespace('Owners', description='owner related operations')
    owners = api.model('Owners', {
        'ownerid': fields.Integer(required=True, description='ownerid'),
        'ownername': fields.String(required=True, description='ownername'),
        'address1': fields.String(required=True, description='address1'),
        'address2': fields.String(required=True, description='address2'),
        'pan': fields.String(required=True, description='pan'),
        'aadhar': fields.String(required=True, description='aadhar'),
        'mobile': fields.String(required=True, description='mobile'),
        'gst': fields.String(required=True, description='gst'),
        'startdate': fields.DateTime(required=True, description='startdate'),
        'enddate': fields.DateTime(required=True, description='enddate'),
        'dlno': fields.String(required=True, description='dlno'),
        'isactive': fields.Boolean(required=True, description='isactive'),
        'status': fields.String(required=True, description='status'),
        'statuschangedate': fields.DateTime(required=True, description='statuschangedate'),
        'stateid': fields.Integer(required=True, description='stateid'),
        'state': fields.String(required=True, description='state'),
        'pincode': fields.String(required=True, description='pincode'),
        'bankname': fields.String(required=True, description='bankname'),
        'accountno': fields.String(required=True, description='accountno'),
        'ifsc': fields.String(required=True, description='ifsc'),
        'transportercode': fields.String(required=True, description='transportercode')
    })

class WeighbridgeDto:
    api = Namespace('Weighbridge', description='Weighbridge related operations')
    weighbridge = api.model('Weighbridge', {
        'wbid': fields.Integer(required=True, description='wbid'),
        'wbname': fields.String(required=True, description='wbname'),
        'locationid': fields.Integer(required=True, description='locationid'),
        'location': fields.String(required=True, description='location'),
        'capacity': fields.Integer(required=True, description='capacity')
    })

class DriversDto:
    api = Namespace('Drivers', description='Drivers related operations')
    drivers = api.model('Drivers', {
        'driverid': fields.Integer(description='driver Identifier'),
        'drivername': fields.String(required=True, description='drivername'),
        'dlno': fields.String(required=True, description='dlno'),
        'dltype': fields.String(required=True, description='dltype'),
        'address': fields.String(required=True, description='address'),
        'dlexpiry': fields.DateTime(required=True, description='dlexpiry'),
        'isactive': fields.Boolean(required=True, description='isactive'),
        'drivermobile': fields.String(required=True, description='drivermobile'),
        'fingerprint': fields.String(required=True, description='fingerprint'),
        'faceprint': fields.String(required=True, description='faceprint'),
        'status': fields.String(required=True, description='status'),
        'statuschangedate': fields.DateTime(required=True, description='statuschangedate')
    })

class RfidtagDto:
    api = Namespace('Rfidtag', description='Rfidtag related operations')
    rfidtag = api.model('Rfidtag', {
        'rfid': fields.Integer(description='rfid Identifier'),
        'rfno': fields.String(required=True, description='rfno'),
        'isactive': fields.Boolean(required=True, description='isactive'),
        'issuedate': fields.DateTime(required=True, description='issuedate'),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'vehicleid': fields.Integer(required=True, description='vehicleid')
    })

class IngateDto:
    api = Namespace('Ingate', description='Ingate related operations')
    ingate = api.model('Ingate', {
        'slipid': fields.Integer(required=True, description='slipid'),
        'sliptime': fields.DateTime(required=True, description='sliptime'),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'destination': fields.String(required=True, description='destination'),
        'loading': fields.String(required=True, description='loading'),
        'dlno': fields.String(required=True, description='dlno'),
        'transporter': fields.String(required=True, description='transporter'),
        'gate': fields.String(required=True, description='gate'),
        'currentlogin': fields.String(required=True, description='currentlogin'),
        'driver': fields.String(required=True, description='driver'),
        'controlno': fields.Integer(required=True, description='controlno'),
        'driverid': fields.Integer(required=True, description='driverid'),
        'tare': fields.Integer(required=True, description='tare'),
        'rfid': fields.Integer(required=True, description='rfid'),
        'rfno': fields.String(required=True, description='rfno'),
        'locationid': fields.Integer(required=True, description='locationid'),
        'transporterid': fields.Integer(required=True, description='transporterid'),
        'vehicleid': fields.Integer(required=True, description='vehicleid'),
        'validslip': fields.Boolean(required=True, description='validslip'),
        'slipno': fields.String(required=True, description='slipno'),
        'quantity': fields.Integer(required=True, description='quantity'),
        'fueltime': fields.DateTime(required=True, description='fueltime'),
        'fueloperator': fields.String(required=True, description='fueloperator'),
        'wheeler': fields.Integer(required=True, description='wheeler')

    })

class VehiclesDto:
    api = Namespace('Vehicles', description='Vehicles related operations')
    vehicles = api.model('Vehicles', {
        'vehicleid': fields.Integer(required=True, description='vehicleid'),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'compliant': fields.Integer(required=True, description='compliant'),
        'ownerid': fields.Integer(required=True, description='ownerid'),
        'ownername': fields.String(required=True, description='ownername'),
        'ownermobile': fields.String(required=True, description='ownermobile'),
        'rcno': fields.String(required=True, description='rcno'),
        'tempno': fields.String(required=True, description='tempno'),
        'chasisno': fields.String(required=True, description='chasisno'),
        'fitnessexpiry': fields.DateTime(required=True, description='fitnessexpiry'),
        'insuranceexpiry': fields.DateTime(required=True, description='insuranceexpiry'),
        'permitexpiry': fields.DateTime(required=True, description='permitexpiry'),
        'pollutionexpiry': fields.DateTime(required=True, description='pollutionexpiry'),
        'permittype': fields.String(required=True, description='permittype'),
        'status': fields.String(required=True, description='status'),
        'statuschangedate': fields.DateTime(required=True, description='statuschangedate'),
        'createdate': fields.DateTime(required=True, description='createdate'),
        'ownerpan': fields.String(required=True, description='ownerpan'),
        'rfno': fields.String(required=True, description='rfno'),
        'permit': fields.String(required=True, description='permit'),
        'insurance': fields.String(required=True, description='insurance'),
        'pollution': fields.String(required=True, description='pollution'),
        'fitness': fields.String(required=True, description='fitness'),
        'isactive': fields.Boolean(required=True, description='isactive'),
        'roadtax': fields.String(required=True, description='roadtax'),
        'roadtaxexpiry': fields.DateTime(required=True, description='roadtaxexpiry'),
        'rcdate ': fields.DateTime(required=True, description='rcdate '),
        'wheeler': fields.Integer(required=True, description='wheeler'),
        'vowner': fields.String(required=True, description='vowner'),
        'vcontact': fields.String(required=True, description='vcontact'),
        'vaddress': fields.String(required=True, description='vaddress'),
        'vownership': fields.Boolean(required=True, description='vownership'),
        'gpsdate': fields.DateTime(required=True, description='gpsdate'),
        'gpsno': fields.String(required=True, description='gpsno'),
        'imeino': fields.String(required=True, description='imeino'),
        'modelno': fields.String(required=True, description='modelno'),
        'engine': fields.String(required=True, description='engine')
    })  

class RailwaysidingDto:
    api = Namespace('Railwaysiding', description='Railwaysiding related operations')
    railwaysiding = api.model('Railwaysiding', {
        'entryid': fields.Integer(required=True, description='entryid'),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'grosswb': fields.String(required=True, description='grosswb'),
        'gross': fields.Integer(required=True, description='gross'),
        'tarewb': fields.String(required=True, description='tarewb'),
        'tare': fields.Integer(required=True, description='tare'),
        'net': fields.Integer(required=True, description='net'),
        'entrytime': fields.DateTime(required=True, description='entrytime'),
        'shortage': fields.Integer(required=True, description='shortage'),
        'exittime': fields.DateTime(required=True, description='exittime'),
        'remarks': fields.String(required=True, description='remarks'),
        'vehicleid': fields.Integer(required=True, description='vehicleid'),
        'challannet': fields.Integer(required=True, description='challannet'),
        'challanno': fields.String(required=True, description='challanno'),
        'slipno': fields.String(required=True, description='slipno'),
        'grosswbid': fields.Integer(required=True, description='grosswbid'),
        'tarewbid': fields.Integer(required=True, description='tarewbid'),
        'usergross': fields.String(required=True, description='usergross'),
        'usertare': fields.String(required=True, description='usertare'),
        'userexit': fields.String(required=True, description='usertare'),
        'wbdatetime': fields.DateTime(required=True, description='entrytime')
        
    })

class OutgateDto:
    api = Namespace('Outgate', description='Outgate related operations')
    outgate = api.model('Outgate', {
        'challanid': fields.Integer(required=True, description='challanid'),
        'slipno': fields.String(required=True, description='slipno'),
        'slipid': fields.Integer(required=True, description='slipid '),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'driver': fields.String(required=True, description='driver'),
        'driverid': fields.Integer(required=True, description='driverid'),
        'loading': fields.String(required=True, description='loading'),
        'destination': fields.String(required=True, description='destination'),
        'challanno': fields.String(required=True, description='challanno'),
        'gross': fields.Integer(required=True, description='gross'),
        'tare': fields.Integer(required=True, description='tare'),
        'net': fields.Integer(required=True, description='net'),
        'passdate': fields.DateTime(required=True, description='passdate'),
        'passgate': fields.String(required=True, description='passgate'),
        'sliptime': fields.DateTime(required=True, description='sliptime'),
        'challantime': fields.DateTime(required=True, description='challantime'),
        'printtime': fields.DateTime(required=True, description='printtime'),
        'material': fields.String(required=True, description='material'),
        'weighbridge': fields.String(required=True, description='weighbridge'),
        'vehicleid': fields.Integer(required=True, description='vehicleid'),
        'locationid': fields.Integer(required=True, description='locationid'),
        'username': fields.String(required=True, description='username'),
        'transporterid': fields.Integer(required=True, description='transporterid'),
        'transporter': fields.String(required=True, description='transporter'),
        'challannet': fields.Integer(required=True, description='challannet'),
        'grosswbid': fields.Integer(required=True, description='grosswbid'),
        'grosswb': fields.String(required=True, description='grosswb'),
        'tarewbid': fields.Integer(required=True, description='tarewbid'),
        'tarewb': fields.String(required=True, description='tarewb'),
        'passusername': fields.String(required=True, description='passusername'),
        'wbdatetime': fields.DateTime(required=True, description='wbdatetime')

    }) 

class FuelgateDto:
    api = Namespace('Fuelgate', description='Fuelgate related operations')
    fuelgate = api.model('Fuelgate', {
        'fuelid': fields.Integer(required=True, description='fuelid'),
        'vehicleno': fields.String(required=True, description='vehicleno'),
        'slipno': fields.String(required=True, description='slipno'),
        'challanno': fields.String(required=True, description='challanno'),
        'quantity': fields.Integer(required=True, description='quantity'),
        'fueltime': fields.DateTime(required=True, description='fueltime'),
        'vehicleid': fields.Integer(required=True, description='vehicleid'),
        'fuelslipno': fields.String(required=True, description='fuelslipno'),
        'username': fields.String(required=True, description='username'),
        'slipid': fields.Integer(required=True, description='slipid'),
        'transporter': fields.String(required=True, description='transporter'),
        'transporterid': fields.Integer(required=True, description='transporterid'),
        'location': fields.String(required=True, description='location'),
        'locationid': fields.Integer(required=True, description='locationid'),
        'wheeler': fields.Integer(required=True, description='wheeler'),
        'driver': fields.String(required=True, description='driver'),
        'driverid': fields.Integer(required=True, description='driverid'),
        'fuelbyrule': fields.Integer(required=True, description='driverid')

    }) 

class UserPermissionsDto:
    api = Namespace('UserPermissions', description='UserPermissions related operations')
    userpermissions = api.model('UserPermissions', {
        'UserPermissionId': fields.Integer(required=True, description='UserPermissionId'),
        'UserId': fields.Integer(required=True, description='UserId'),
        'PermissionKey': fields.String(required=True, description='PermissionKey'),
        'Granted': fields.Boolean(required=True, description='Granted')
    }) 

class CategoryDto:
    api = Namespace('Category', description='Category related operations')
    category = api.model('Category', {
        'categoryid': fields.Integer(required=True, description='categoryid'),
        'categoryname': fields.String(required=True, description='categoryname'),
        'parentid': fields.Integer(required=True, description='parentid')
    }) 

class AssetsDto:
    api = Namespace('Assets', description='Assets related operations')
    assets = api.model('Assets', {
        'assetid': fields.Integer(required=True, description='assetid'),
        'assetname': fields.String(required=True, description='assetname'),
        'category': fields.String(required=True, description='category'),
        'make': fields.String(required=True, description='make'),
        'model': fields.String(required=True, description='model'),
        'serialno': fields.String(required=True, description='serialno'),
        'location': fields.String(required=True, description='location'),
        'intallationdate': fields.DateTime(required=True, description='intallationdate'),
        'assetcode': fields.String(required=True, description='assetcode'),
        'status': fields.String(required=True, description='status'),
        'statuschangedate': fields.DateTime(required=True, description='statuschangedate'),
        'categoryid': fields.Integer(required=True, description='categoryid'),
        'locationid': fields.Integer(required=True, description='locationid')
    })

class CompanyDto:
    api = Namespace('Company', description='Company related operations')
    Company = api.model('Company', {
        'cid': fields.Integer(required=True, description='cid'),
        'cname': fields.String(required=True, description='cname'),
        'address1': fields.String(required=True, description='address1'),
        'address2': fields.String(required=True, description='address2'),
        'phone': fields.String(required=True, description='phone')
    })

class fuelmasterDto:
    api = Namespace('fuelmaster', description='fuelmaster related operations')
    fuelmaster = api.model('fuelmaster', {
        'fuelid': fields.Integer(required=True, description='fuelid'),
        'wheels': fields.Integer(required=True, description='wheels'),
        'fuelpermt': fields.Integer(required=True, description='fuelpermt'),
        'effectivefrom': fields.DateTime(required=True, description='effectivefrom')
    })

class RolePermissionsDto:
    api = Namespace('RolePermissions', description='RolePermissions related operations')
    RolePermissions = api.model('RolePermissions', {
        'RolePermissionId': fields.Integer(required=True, description='RolePermissionId'),
        'RoleId': fields.Integer(required=True, description='RoleId'),
        'PermissionKey': fields.String(required=True, description='PermissionKey')
    })

class RolesDto:
    api = Namespace('Roles', description='Roles related operations')
    Roles = api.model('Roles', {
        'RoleId': fields.Integer(required=True, description='RoleId'),
        'RoleName': fields.String(required=True, description='RoleName')
    }) 

class UserRolesDto:
    api = Namespace('UserRoles', description='UserRoles related operations')
    UserRoles = api.model('UserRoles', {
        'UserRoleId': fields.Integer(required=True, description='UserRoleId'),
        'UserId': fields.Integer(required=True, description='UserId'),
        'RoleId': fields.Integer(required=True, description='RoleId')
    })

class users_appDto:
    api = Namespace('users_app', description='users_app related operations')
    users_app = api.model('users_app', {
        'id': fields.Integer(required=True,description='id'),
        'user_name': fields.String(required=True, description='user_name'),
        'password': fields.String(required=True, description='password'),
        'is_active': fields.Boolean(required=True, description='is_active'),
        'display_name': fields.String(required=True, description='display_name'),
        'create_date': fields.DateTime(required=True, description='create_date'),
        'public_id': fields.Integer(required=True, description='public_id'),
        'admin': fields.Boolean(required=True, description='admin'),
    })

