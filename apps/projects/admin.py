from django.contrib import admin
from .models import Project, Category,ProjectImage,Experiment,Datarow
from django.utils import html
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.urls import reverse

'''
for more information and dokumentation check 
docs.djangoproject.com/en/dev/ref/contrib/admin/
'''


class ProjectImagesInline (admin.TabularInline):
    '''
    Inline for Project Images
    '''

    '''Shows Images'''
    def get_projetc_images(instance):
        if not instance.path:
            return
        return html.format_html("""<img src="{src}" style="max-width: 200px; max-height: 200px;" />""",
                                src='/' + instance.path.url,
                                )
    '''show Link to ProjectImages admin Site'''
    def get_edit_link(self, instance):
        if not instance.path:
            return

        url = reverse('admin:%s_%s_change' % (instance._meta.app_label, instance._meta.model_name),
                      args=[force_text(instance.id)])

        return html.format_html("""<a href="{url}">{text}</a>""".format(
                url=url,
                text="Ändere Bild %s auf Seperaten Seite" % instance._meta.verbose_name,
        ))

    get_edit_link.short_description = _('project image link')

    '''Translate project Images in Project'''
    get_projetc_images.short_description = _('project images')

    '''Attributes for Inline'''
    model = ProjectImage
    verbose_name = _('project')
    verbose_name_plural = _('projects')
    fk_name = 'project'
    can_delete = False
    extra = 0
    fieldsets = ((_('project images'),{'fields':('get_edit_link', get_projetc_images)}),)
    readonly_fields = ('get_edit_link', get_projetc_images,)


class ExperimentInline(admin.StackedInline):
    '''
        Inline for Experiments in Project
    '''


    pass


class DatarowInline(admin.StackedInline):
    '''
        Inline for Datarows in Experiment
    '''



    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    """ The Project admin model.
    Attributes:
        See django.contrib.auth.models.AbstractUser.
        fieldsets: The fieldset to show in the admin.
        list_display: The data to show in the list.
        search_fields: To filter
    """
    list_display = ('name',
                    'category',
                    'subcategory',
                    'manufacturer',
                    'visibility',)

    readonly_fields = ('created',
                       'updated',
                       'measured',
                       )

    """ search_fields: Filter Searchfield.
        list_filter: Filter Checkbox visibility 
    """
    search_fields = ['name',
                     'category__name',
                     'subcategory__name',
                     'manufacturer',
                     'user__username',
                     'description',
                     'typ',
                     'experiment__name',
                     ]
    list_filter = ('visibility',)

    '''fieldset: fields inside Project'''
    fieldsets = (
        (_('info'), {'fields': ('name', 'user', 'visibility',)}),
        (_('attributes'), {'fields': ('category', 'subcategory', 'manufacturer', 'typ','description',)}),
        (_('important dates'), {'fields': ('created', 'updated','measured')}),
    )

    inlines = [ProjectImagesInline,]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''list_display: The data to show in the list.'''
    list_display = ('name',
                    'parent')

    """ search_fields: Filter Searchfield."""
    search_fields = ['name',
                     'parent__name'
                     ]

@admin.register(ProjectImage)
class ProjetcImageAdmin(admin.ModelAdmin):

    """ The ProjectImage admin.
        change or delete ProjetcImage
    """

    def get_project_image(instance):
        if not instance.path:
            return
        return html.format_html("""<img src="{src}" style="max-width: 200px; max-height: 200px;" />""",
                                src='/' + instance.path.url,
                                )
    '''Translate Project Image in ProjectImage'''
    get_project_image.short_description = _('projetc image')
    save_on_top = True
    fields = ('path',
              get_project_image)

    readonly_fields = (get_project_image,)

class ExperimentAdmin(admin.ModelAdmin):
    """ The Experiment admin.
              change or delete Experiments
           """
    pass


class DatarowAdmin(admin.ModelAdmin):
    """ The Datarow admin.
              change or delete Datarow
           """
    pass

