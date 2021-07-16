from django.contrib.admin import SimpleListFilter


class SubjectsTaughtFilter(SimpleListFilter):
    title = 'Subject'
    parameter_name = 'subjects_taught'

    def lookups(self, request, model_admin):
        subjects_taught = set([
            i.subjects_taught for i in model_admin.model.objects.all() if i.subjects_taught
        ])
        result = set([
            (x.lower().strip(), x.strip().capitalize()) for i in subjects_taught for x in i.split(',')
        ])
        return result

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subjects_taught__contains=self.value())


class LastNameFilter(SimpleListFilter):
    title = 'First litter of last_name'
    parameter_name = 'last_name'

    def lookups(self, request, model_admin):
        last_name = set([i.last_name for i in model_admin.model.objects.all() if i.last_name])
        return set([(i[0].lower(), i[0].capitalize()) for i in last_name])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(last_name__startswith=self.value())
