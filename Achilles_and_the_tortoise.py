# تعريف المتغيرات
distance_initial = 100  # المسافة الأولية بين أخيل والسلحفاة
achilles_speed = 10  # سرعة أخيل
tortoise_speed = 1  # سرعة السلحفاة

# الزمن الذي يحتاجه أخيل للوصول إلى نقطة البداية للسلحفاة
time_to_initial_point = distance_initial / achilles_speed

# المسافة التي تقطعها السلحفاة خلال هذا الزمن
tortoise_new_distance = tortoise_speed * time_to_initial_point

# المتغيرات الأولية
total_distance_achilles = 0
total_time = 0

# عدد الخطوات التي نريد محاكاتها
steps = 10

# عملية حساب مجموع السلسلة الهندسية
for step in range(steps):
    time_to_reach_tortoise = tortoise_new_distance / achilles_speed
    total_time += time_to_reach_tortoise
    total_distance_achilles += tortoise_new_distance

    print(f"Step {step + 1}:")
    print(f"Achilles reaches the point where the tortoise was.")
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Total distance by Achilles: {total_distance_achilles:.6f} meters\n")

    # حساب المسافة الجديدة التي تتحركها السلحفاة
    tortoise_new_distance = tortoise_speed * time_to_reach_tortoise

# النتيجة النهائية
print(f"Final Total Time: {total_time:.6f} seconds")
print(f"Final Total Distance by Achilles: {total_distance_achilles + distance_initial:.6f} meters")
