# دليل التركيب + إزاي تملّى الجراف وتاخد الشارات

## 1) التركيب (من Termux)
1. على GitHub اعمل ريبو **Public** اسمه بالظبط: `mohamedghanem-dev` (نفس اسم حسابك) وحط فيه README.
2. فك الملفات في فولدر الريبو وارفعها:
```bash
git clone https://github.com/mohamedghanem-dev/mohamedghanem-dev
cd mohamedghanem-dev
# انسخ محتويات الـ zip هنا (README.md, assets, .github, scripts)
git add . && git commit -m "feat: new profile" && git push
```
3. من تبويب Actions شغّل يدوي: **Contribution Snake** ثم **Update Recent Projects** (Run workflow).
4. Settings > Actions > General > Workflow permissions = **Read and write**.
5. غيّر مشاريع جدول Featured بأسماء ريبوهاتك الحقيقية، وثبّت (Pin) نفس الـ6 على البروفايل.
6. تحب شكل تاني؟ انسخ محتوى `variants/README-minimal.md` أو `README-bento.md` مكان README.md.

## 2) ليه الجراف مش أخضر رغم إنك بترفع كل يوم؟ (الأسباب الحقيقية)
افحص بالترتيب:
- **إيميل الكوميت**: GitHub بيحسب الكوميت بس لو الإيميل بتاعه مضاف ومتأكد في حسابك.
  `git log -1 --format=%ae` لو الإيميل غريب (Termux/proot كتير بيحط إيميل افتراضي) صلّحه:
  `git config --global user.email "mohamedghanemfs99@gmail.com"`
  وضيف نفس الإيميل في Settings > Emails وأكّده. الكوميتات القديمة بنفس الإيميل بتظهر بعدها.
- **الفرع**: بيتحسب بس الكوميت على الـ default branch (أو gh-pages).
- **Fork**: الكوميت جوه fork مش بيتحسب (إلا بعد Pull Request متدمج للأصل).
- **ريبوهات Private**: من قايمة الجراف فعّل **Private contributions**.
- **الرفع بالمتصفح** بيتحسب عادي، بس لازم الإيميل يطابق.
- **درجة الأخضر نسبية**: الدرجات بتتحدد بالنسبة لأعلى يوم عندك. كوميت واحد في اليوم = أفتح درجة. عشان يغمق: كوميتات صغيرة ومتفرقة طول اليوم، Pull Requests، Issues، Code reviews، وشغل على نفس الريبو بدل رفعه مرة واحدة.

الأتمتة اللي في المثال التاني (`daily-activity.yml`) بتكتب سطر في ملف log كل 6 ساعات عشان تملّى الجراف. ماحطتهاش في الباكدج: ظاهرة في الكوميتات وأي مراجع بيعرفها ويقلل ثقة العميل، وبتلخبط الجراف الحقيقي بتاعك. الأقوى إنك تستعمل الإصلاحات فوق وتشتغل بكوميتات صغيرة حقيقية.

## 3) الشارات (Achievements) بشكل طبيعي
بتظهر لوحدها في البروفايل، والمفيد إنك تستخدم workflow احترافي حتى في ريبوهاتك:
- **Pull Shark**: 2 Pull Requests متدمجة (اشتغل بفرع feature ثم PR ثم Merge حتى في ريبوهاتك).
- **YOLO**: دمج PR من غير review.
- **Quickdraw**: قفل Issue أو PR خلال 5 دقايق من فتحه.
- **Pair Extraordinaire**: كوميت فيه `Co-authored-by:` لشخص حقيقي في PR متدمج.
- **Galaxy Brain**: إجابات مقبولة في GitHub Discussions.
- **Starstruck**: ريبو يوصل 16 نجمة، يعني README قوي + Screenshots + مشاركة المشروع.
- شارات Sponsors/Mars وغيرها حسب الظروف. راجع المطلوب الحالي في توثيق GitHub لأنه بيتغير.

## 4) نصايح تخليك أميز من الأمثلة
- الأمثلة فيها أرقام "مبالغ فيها" (مثلا Projects 95+ أو "Level-07"). البروفايل ده بياناته حية من حسابك فهو أصدق.
- فعّل **Pin** لأفضل 6 مشاريع وحط لكل ريبو: وصف، Topics، Screenshot، ولينك Live demo.
- اعمل ريبو README لكل مشروع بصورة/GIF، لأن العميل بيدخل مشروع واحد ويحكم.
- ضيف رابط LinkedIn وواتساب في القسم المعلّق بآخر README (محطوط كتعليق).
