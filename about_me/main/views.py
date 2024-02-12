from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Profile, Skill


def index(request):
    """Главная страница."""
    template = "index.html"
    profiles = Profile.objects.select_related("skill").all()
    context = {}
    context['profiles'] = profiles
    return render(request, template, context)


def profiles_by_skill(request, slug):
    """Страница с профилями с конкретным скилом."""
    skill = get_object_or_404(Skill, slug=slug)

    # profiles = Profile.objects.filter(skill_id=skill.id)

    profiles = skill.profiles.all()
    context = {}
    context['profiles'] = profiles
    context['skill'] = skill

    return render(request, "skills.html", context)
