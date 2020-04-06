# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Efficacy(models.Model):
    efficacy_no = models.CharField(db_column='efficacy_No', primary_key=True, max_length=10)  # Field name made lowercase.
    eff_name = models.CharField(db_column='eff_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eff_intro = models.CharField(max_length=255, blank=True, null=True)
    med_mat_no = models.ForeignKey('MedMat', models.DO_NOTHING, db_column='med_mat No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recipe_no = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='recipe_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'efficacy'


class Gene(models.Model):
    gene_no = models.CharField(db_column='gene_No', primary_key=True, max_length=10)  # Field name made lowercase.
    gene_name = models.CharField(db_column='gene_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gene_cat = models.CharField(max_length=255, blank=True, null=True)
    gene_alias = models.CharField(max_length=255, blank=True, null=True)
    gene_intro = models.CharField(max_length=255)
    ch_location = models.CharField(max_length=255, blank=True, null=True)
    marker_no = models.ForeignKey('Marker', models.DO_NOTHING, db_column='marker_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'gene'


class Illness(models.Model):
    illness_no = models.CharField(db_column='illness_No', primary_key=True, max_length=10)  # Field name made lowercase.
    illness_name = models.CharField(db_column='illness_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ill_intro = models.CharField(max_length=255, blank=True, null=True)
    recipe_no = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='recipe_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'illness'


class Marker(models.Model):
    marker_no = models.CharField(db_column='marker_No', primary_key=True, max_length=10)  # Field name made lowercase.
    marker_name = models.CharField(db_column='marker_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    marker_cat = models.CharField(max_length=255, blank=True, null=True)
    marker_intro = models.CharField(max_length=255, blank=True, null=True)
    illness_no = models.ForeignKey(Illness, models.DO_NOTHING, db_column='illness_No', blank=True, null=True)  # Field name made lowercase.
    med_mat_no = models.ForeignKey('MedMat', models.DO_NOTHING, db_column='med_mat_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'marker'


class MedMat(models.Model):
    med_mat_no = models.CharField(db_column='med_mat No', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    category = models.CharField(max_length=255, blank=True, null=True)
    dosage = models.CharField(max_length=255, blank=True, null=True)
    med_intro = models.CharField(max_length=255, blank=True, null=True)
    med_mat_name = models.CharField(db_column='med_mat Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recipe_no = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='recipe_No', blank=True, null=True)  # Field name made lowercase.
    med_mat_Latin_name = models.CharField(db_column='med_mat Latin_Name', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'med_mat'


class Molecule(models.Model):
    molecule_no = models.CharField(db_column='molecule_No', primary_key=True, max_length=10)  # Field name made lowercase.
    molecule_name = models.CharField(db_column='molecule_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    molecule_formula = models.CharField(max_length=255, blank=True, null=True)
    molar_mass = models.CharField(db_column='molar mass', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    molecule_str = models.CharField(max_length=255, blank=True, null=True)
    synonyms = models.CharField(max_length=255, blank=True, null=True)
    marker_no = models.ForeignKey(Marker, models.DO_NOTHING, db_column='marker_No', blank=True, null=True)  # Field name made lowercase.
    med_mat_no = models.ForeignKey(MedMat, models.DO_NOTHING, db_column='med_mat No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'molecule'


class Recipe(models.Model):
    recipe_no = models.CharField(db_column='recipe_No', primary_key=True, max_length=10)  # Field name made lowercase.
    recipe_name = models.CharField(db_column='recipe_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fangyi = models.CharField(max_length=500, blank=True, null=True)
    classify = models.CharField(max_length=255, blank=True, null=True)
    for_in_verse = models.CharField(max_length=255, blank=True, null=True)
    comprise = models.CharField(max_length=255, blank=True, null=True)
    provenance = models.CharField(max_length=255, blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recipe'

    def __str__(self):
        return self.recipe_name


class Symptom(models.Model):
    symptom_no = models.CharField(db_column='symptom_No', primary_key=True, max_length=10)  # Field name made lowercase.
    symptom_name = models.CharField(db_column='symptom_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    symptom_per = models.CharField(max_length=255, blank=True, null=True)
    sym_med_no = models.CharField(db_column='sym_med_No', max_length=10, blank=True, null=True)  # Field name made lowercase.
    illness_no = models.ForeignKey(Illness, models.DO_NOTHING, db_column='illness_No', blank=True, null=True)  # Field name made lowercase.
    recipe_no = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='recipe_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'symptom'
