# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PmpModel(models.Model):
    pmp_model_nm = models.CharField(db_column='PMP_MODEL_NM',primary_key=True, max_length=50)  
    pmp_type = models.CharField(db_column='PMP_TYPE', max_length=50, blank=True, null=True)  
    bore = models.CharField(db_column='BORE', max_length=50, blank=True, null=True)  
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  

    class Meta:
        #managed = False
        db_table = 'pmp_model'


class SiteInfo(models.Model):
    site_id = models.CharField(db_column='SITE_ID', primary_key=True, max_length=50)  
    site_nm = models.CharField(db_column='SITE_NM', max_length=50, blank=True, null=True)  
    site_addr = models.CharField(db_column='SITE_ADDR', max_length=50, blank=True, null=True)  
    manu_comp_nm = models.CharField(db_column='MANU_COMP_NM', max_length=50, blank=True, null=True)  
    manu_comp_phone = models.CharField(db_column='MANU_COMP_PHONE', max_length=50, blank=True, null=True)  
    deli_comp_nm = models.CharField(db_column='DELI_COMP_NM', max_length=50, blank=True, null=True)  
    deli_comp_phone = models.CharField(db_column='DELI_COMP_PHONE', max_length=50, blank=True, null=True)  
    manu_dt = models.DateTimeField(db_column='MANU_DT', blank=True, null=True)  
    free_srv_st_dt = models.DateTimeField(db_column='FREE_SRV_ST_DT', blank=True, null=True)  
    free_srv_end_dt = models.DateTimeField(db_column='FREE_SRV_END_DT', blank=True, null=True)  
    paid_srv_comp_nm = models.CharField(db_column='PAID_SRV_COMP_NM', max_length=50, blank=True, null=True)  
    paid_srv_comp_phone = models.CharField(db_column='PAID_SRV_COMP_PHONE', max_length=50, blank=True, null=True)  
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  

    class Meta:
        #managed = False
        db_table = 'site_info'


class SitePmp(models.Model):
    site_id = models.ForeignKey(SiteInfo, models.DO_NOTHING, db_column='SITE_ID',related_name='site_pmp_site_id')  
    pmp_manu_num = models.CharField(db_column='PMP_MANU_NUM', primary_key=True, max_length=50)  
    pmp_model_nm = models.CharField(db_column='PMP_MODEL_NM', max_length=50)  
    pmp_type = models.CharField(db_column='PMP_TYPE', max_length=50, blank=True, null=True)  
    bore = models.CharField(db_column='BORE', max_length=50, blank=True, null=True)  
    head = models.CharField(db_column='HEAD', max_length=50, blank=True, null=True)  
    capacity = models.CharField(db_column='CAPACITY', max_length=50, blank=True, null=True)  
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  

    class Meta:
        #managed = False
        db_table = 'site_pmp'


class PmpRepairHistory(models.Model):
    site_id = models.ForeignKey(SitePmp, models.DO_NOTHING, db_column='SITE_ID',related_name= 'pmp_repair_history_site_id')  
    pmp_manu_num = models.ForeignKey(SitePmp, models.DO_NOTHING, db_column='PMP_MANU_NUM',related_name='pmp_repair_history_pmp_manu_num')  
    visit_engineer_nm = models.CharField(db_column='VISIT_ENGINEER_NM', max_length=50, blank=True, null=True)  
    visit_engineer_phone = models.CharField(db_column='VISIT_ENGINEER_PHONE', max_length=50, blank=True, null=True)  
    repair_contents = models.CharField(db_column='REPAIR_CONTENTS', max_length=50, blank=True, null=True)  
    visit_date = models.DateTimeField(db_column='VISIT_DATE', blank=True, null=True)  
    create_dt = models.DateTimeField(db_column='CREATE_DT', blank=True, null=True)  

    class Meta:
        #managed = False
        db_table = 'pmp_repair_history'
