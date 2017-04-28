from django.core.urlresolvers import RegexURLResolver, RegexURLPattern


def recursively_build__url_dict(d, urlpatterns):
    for i in urlpatterns:
        if isinstance(i, RegexURLResolver):
            d[str(i.__dict__['_regex'])] = {}
            if str(i.__dict__['_regex']) != "^admin/":
                recursively_build__url_dict(
                    d[str(i.__dict__['_regex'])], i.url_patterns
                )
            else:
                d[str(i.__dict__['_regex'])] = "REDACTED"

        elif isinstance(i, RegexURLPattern):
                d[str(i.regex.pattern)] = i.callback.__name__
