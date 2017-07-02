from series.models import Series


def copy_series(qs=Series.objects.all()):
	if qs.count() < 100:
		for obj in qs:
			title = obj.title
			image = obj.image
			category = obj.category
			secondary_category = obj.secondary.all()
			description = obj.description
			new_obj = Series.objects.create(
					title = title,
					image = image,
					category = category,
					description = description,
				)
			for cat in secondary:
				new_obj.secondary.add()
			new_obj.save()
		qs2 = Series.objects.all()
		if qs2.count() <= 100:
			return copy_series(qs=qs2)
	return qs.count()