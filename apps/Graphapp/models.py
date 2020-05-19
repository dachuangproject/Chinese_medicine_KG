# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Gene(models.Model):
    gene_no = models.CharField(db_column='gene_No', primary_key=True, max_length=10)  # Field name made lowercase.
    gene_name = models.CharField(db_column='gene_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gene_cat = models.CharField(max_length=255, blank=True, null=True)
    gene_alias = models.CharField(max_length=255, blank=True, null=True)
    gene_intro = models.CharField(max_length=255)
    ch_location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gene'


class Diseases(models.Model):
    diseases_no = models.CharField(db_column='diseases_No', primary_key=True, max_length=10)  # Field name made lowercase.
    diseases_name = models.CharField(db_column='diseases_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diseases_intro = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diseases'


class Target(models.Model):
    target_no = models.CharField(db_column='target_No', primary_key=True, max_length=10)  # Field name made lowercase.
    target_name = models.CharField(db_column='target_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    target_cat = models.CharField(max_length=255, blank=True, null=True)
    target_intro = models.CharField(max_length=255, blank=True, null=True)
    diseasesName = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'target'

class Forcom(models.Model):
    forcom_no = models.CharField(db_column='forcom_No', primary_key=True, max_length=10)
    dosage1= models.CharField(max_length=255, blank=True, null=True)
    dosage2= models.CharField(max_length=255, blank=True, null=True)
    mark= models.CharField(max_length=255, blank=True, null=True)
    formulas_no= models.CharField(db_column='formulas_No',max_length=10, blank=True, null=True)
    herbs_name= models.CharField(db_column='herbs_Name',max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'forcom'

class Herbs(models.Model):
    herbs_no = models.CharField(db_column='herbs_No', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    herbs_intro = models.CharField(max_length=255, blank=True, null=True)
    herbs_name = models.CharField(db_column='herbs_Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    treatill= models.CharField(max_length=255, blank=True, null=True)
    medclassify=models.IntegerField( blank=True, null=True)
    taste= models.CharField(max_length=255, blank=True, null=True)
    usdosage= models.CharField(max_length=255, blank=True, null=True)
    plcha= models.CharField(max_length=511, blank=True, null=True)
    plenvir= models.CharField(max_length=255, blank=True, null=True)
    distribute= models.CharField(max_length=255, blank=True, null=True)
    function= models.CharField(db_column='functions',max_length=255, blank=True, null=True)
    machine= models.CharField(max_length=255, blank=True, null=True)
    discuss= models.CharField(max_length=255, blank=True, null=True)
    alias= models.CharField(max_length=255, blank=True, null=True)
    plclassify= models.CharField(max_length=255, blank=True, null=True)
    compa = models.CharField(max_length=255, blank=True, null=True)
    pinyin = models.CharField(max_length=255, blank=True, null=True)
    toxicity= models.CharField(max_length=255, blank=True, null=True)
    attention= models.CharField(max_length=511, blank=True, null=True)
    medfun= models.CharField(max_length=255, blank=True, null=True)
    checom= models.CharField(max_length=255, blank=True, null=True)
    pmethod= models.CharField(max_length=255, blank=True, null=True)
    annotation= models.CharField(max_length=255, blank=True, null=True)
    capplication= models.CharField(max_length=255, blank=True, null=True)
    anicha= models.CharField(max_length=255, blank=True, null=True)
    stomethod= models.CharField(max_length=255, blank=True, null=True)
    growth = models.CharField(max_length=255, blank=True, null=True)
    statement = models.CharField(max_length=255, blank=True, null=True)
    cultech = models.CharField(max_length=255, blank=True, null=True)
    modesofrepro= models.CharField(max_length=255, blank=True, null=True)
    anikind= models.CharField(max_length=255, blank=True, null=True)
    latin= models.CharField(max_length=255, blank=True, null=True)
    bcpre= models.CharField(max_length=511, blank=True, null=True)
    plregion= models.CharField(max_length=255, blank=True, null=True)
    taboo= models.CharField(max_length=255, blank=True, null=True)
    manmade= models.CharField(max_length=255, blank=True, null=True)
    modresearch = models.CharField(max_length=255, blank=True, null=True)
    resourcedis = models.CharField(max_length=255, blank=True, null=True)
    mineralcha = models.CharField(max_length=255, blank=True, null=True)
    mineralkind= models.CharField(max_length=255, blank=True, null=True)
    mineralenvir= models.CharField(max_length=255, blank=True, null=True)
    aniregion= models.CharField(max_length=255, blank=True, null=True)
    mineralnat= models.CharField(max_length=255, blank=True, null=True)
    mainkind= models.CharField(max_length=255, blank=True, null=True)
    proarea= models.CharField(max_length=255, blank=True, null=True)
    toxeffect= models.CharField(max_length=255, blank=True, null=True)
    adverserea= models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'herbs'



class Molecule(models.Model):
    molecule_no = models.CharField(db_column='molecule_No', primary_key=True, max_length=10)  # Field name made lowercase.
    molecule_name = models.CharField(db_column='molecule_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    molecule_formula = models.CharField(max_length=255, blank=True, null=True)
    ML = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    AlogP = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    Hdon = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    Hacc = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    OB = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    Caco = models.DecimalField(db_column='Caco-2',max_digits=20, decimal_places=2,blank=True, null=True) #Caco-2
    BBB = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    DL = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    FASA = models.DecimalField(db_column='FASA-',max_digits=20, decimal_places=2,blank=True, null=True)#FASA-
    HL = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'molecule'


class Formulas(models.Model):
    formulas_no = models.CharField(db_column='formulas_No', primary_key=True, max_length=10)  # Field name made lowercase.
    formulas_name = models.CharField(db_column='formulas_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    composition = models.CharField(max_length=255, blank=True, null=True)
    provenance = models.CharField(max_length=255, blank=True, null=True)
    zhuzhi = models.CharField(max_length=255, blank=True, null=True)
    usage = models.CharField(db_column='usages', max_length=255, blank=True, null=True)
    fufang = models.CharField(max_length=255, blank=True, null=True)
    imliter = models.CharField(max_length=511, blank=True, null=True)
    recfunction=models.CharField(max_length=255, blank=True, null=True)
    fangyi = models.CharField(max_length=511, blank=True, null=True)
    plusedreduced=models.CharField(max_length=255, blank=True, null=True)
    recalias=models.CharField(max_length=255, blank=True, null=True)
    cautioninuse=models.CharField(max_length=255, blank=True, null=True)
    apply=models.CharField(max_length=255, blank=True, null=True)
    for_in_verse = models.CharField(max_length=255, blank=True, null=True)
    compatibilitycha= models.CharField(max_length=255, blank=True, null=True)
    diffdiscuss= models.CharField(max_length=255, blank=True, null=True)
    classify = models.CharField(max_length=255, blank=True, null=True)
    identify= models.CharField(max_length=511, blank=True, null=True)
    recmethod= models.CharField(max_length=255, blank=True, null=True)
    interememory = models.CharField(max_length=255, blank=True, null=True)
    mark= models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'formulas'

    # def __str__(self):
    #     return self.recipe_name



class Tamol(models.Model):
    tgmol_no = models.CharField(db_column='tgmol_No', primary_key=True, max_length=10)  # Field name made lowercase.
    molecular_name = models.CharField(db_column='molecularName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tg_name = models.CharField(db_column='tgName',max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tamol'

class Herbsmol(models.Model):
    herbsmol_no = models.CharField(db_column='herbsmol_No', primary_key=True, max_length=10)  # Field name made lowercase.
    herbs_name = models.CharField(db_column='herbs_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    molecular_name = models.CharField(db_column='molecularName',max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'herbsmol'






