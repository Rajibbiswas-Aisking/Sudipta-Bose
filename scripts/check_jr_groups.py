from website.models import Publication

jr_qs = Publication.objects.filter(category='journal_reviewer').order_by('journal_type','-year')
print('Total journal_reviewer entries:', jr_qs.count())
for key,label in Publication.JOURNAL_TYPE_CHOICES:
    items = list(jr_qs.filter(journal_type=key))
    print(f'Group {label}:', len(items))

untyped = [p for p in jr_qs if not p.journal_type]
print('Untyped count:', len(untyped))
classified = {}
for p in untyped:
    name = (p.journal_or_source or '').lower()
    if 'account' in name:
        classified.setdefault('Accounting Journals',[]).append(p.title)
    elif 'finance' in name:
        classified.setdefault('Finance Journals',[]).append(p.title)
    elif 'econom' in name:
        classified.setdefault('Economics Journals',[]).append(p.title)
    elif 'manage' in name:
        classified.setdefault('Management Journals',[]).append(p.title)
    elif 'conference' in name or 'ad-hoc' in name or 'ad hoc' in name:
        classified.setdefault('Conference reviewer (Adhoc)',[]).append(p.title)
    else:
        classified.setdefault('Other / Unspecified',[]).append(p.title)

print('Classified untyped groups:')
for k,v in classified.items():
    print(k, len(v))
    for t in v:
        print('  -', t)
