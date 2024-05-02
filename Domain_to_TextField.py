import arcpy
import os


def get_gdb_path_of_layer(layer_name):
    aprx = arcpy.mp.ArcGISProject("current")
    mp = aprx.activeMap
    layer = [layer for layer in mp.listLayers() if layer.name == layer_name][0]
    if layer:
        return os.path.dirname(layer.dataSource)
    else:
        return ""


def Domain_to_text(fc, field_name, new_field_name):

    # Extract domain name from field Des
    desc = arcpy.Describe(fc)
    field = [x for x in desc.fields if x.name == feild_name][0]
    field_domain = field.domain

    GDB = get_gdb_path_of_layer(fc)
    # Get the domain from fc GDB
    domain = [x for x in arcpy.da.ListDomains(GDB) if x.name == field_domain][0]
    if domain.domainType != "CodedValue":
        arcpy.AddError(f"Domain {field_domain} is NOT coded value")
        return
    domain_dec = domain.codedValues
    
    arcpy.management.AddField(fc, new_feild_name, "TEXT", None, None, None, new_feild_name, "NULLABLE", "NON_REQUIRED", '')

    with arcpy.da.Editor(GDB) as editor:
        with arcpy.da.UpdateCursor(fc, [field_name, new_field_name]) as cursor:
            for row in cursor:
                for key, val in domain_dec.items():
                    if row[0] == key:
                        row[1] = val
                cursor.updateRow(row)
            
    arcpy.AddMessage('Script Developed by: ENG. Mohamed Mokashifi\n')
    arcpy.AddMessage('Linkedin: https://www.linkedin.com/in/mohamed-mokashifi-adam\n')
    arcpy.AddMessage('GitHub: https://github.com/Eng-Moka')
    arcpy.AddMessage('Gmail: mohamed.mokashifi@gmail.com\n')


if __name__ == '__main__':

    # Tool parameter accessed with GetParameter or GetParameterAsText
    fc = arcpy.GetParameterAsText(0)
    feild_name = arcpy.GetParameterAsText(1)
    new_feild_name = arcpy.GetParameterAsText(2)
    
    Domain_to_text(fc,feild_name,new_feild_name)
    

    
    # Script Developed by: ENG. Mohamed Mokashifi
    # Linkedin: https://www.linkedin.com/in/mohamed-mokashifi-adam
    # GitHub: https://github.com/Eng-Moka
    # Gmail: mohamed.mokashifi@gmail.com
