
XPATH_LOCATORS = [
    # 1. Заголовок главного экрана по тексту и классу
    ("Hero title", "//h1[contains(@class, 'hero-descriptor_title') and normalize-space(text())='Do more!']"),

    # 2. Описание главного экрана
    ("Hero description", "//p[contains(@class, 'hero-descriptor_desc') and contains(text(), 'With the help of the Hillel auto project')]"),

    # 3. Кнопка Sign up по тексту и классу
    ("Sign up button", "//button[contains(@class, 'hero-descriptor_btn') and normalize-space(text())='Sign up']"),

    # 4. Контейнер описания внутри hero
    ("Hero descriptor", "//section[contains(@class, 'hero')]//div[contains(@class, 'hero-descriptor')]"),

    # 5. Видео внутри главного экрана
    ("Hero video", "//section[contains(@class, 'hero')]//div[contains(@class, 'hero-video')]"),

    # 6. Секция About по ID
    ("About section by ID", "//div[@id='aboutSection']"),

    # 7. Секция About по ID и классу
    ("About section by ID and class", "//div[@id='aboutSection' and contains(@class, 'about')]"),

    # 8. Блоки внутри About
    ("About blocks", "//div[@id='aboutSection']//div[contains(@class, 'about-block')]"),

    # 9. Изображение блока About
    ("About picture", "//div[@id='aboutSection']//div[contains(@class, 'about-block_picture')]"),

    # 10. Заголовок Log fuel expenses
    ("Fuel expenses title", "//div[@id='aboutSection']//p[contains(@class, 'about-block_title') and normalize-space(text())='Log fuel expenses']"),

    # 11. Описание Log fuel expenses
    ("Fuel expenses description", "//div[@id='aboutSection']//p[contains(@class, 'about-block_descr') and contains(text(), 'Keep track of your replacement schedule')]"),

    # 12. Секция Contacts по ID
    ("Contacts section by ID", "//div[@id='contactsSection']"),

    # 13. Секция Contacts по ID и классу
    ("Contacts section by ID and class", "//div[@id='contactsSection' and contains(@class, 'contacts')]"),

    # 14. Заголовок Contacts
    ("Contacts heading", "//div[@id='contactsSection']//h2[normalize-space(text())='Contacts']"),

    # 15. Контейнер социальных сетей
    ("Social links container", "//div[@id='contactsSection']//div[contains(@class, 'contacts_socials')]"),

    # 16. Ссылка Facebook по href
    ("Facebook link", "//div[@id='contactsSection']//a[contains(@class, 'socials_link') and contains(@href, 'facebook.com')]"),

    # 17. Ссылка Telegram по href
    ("Telegram link", "//div[@id='contactsSection']//a[contains(@href, 't.me/ithillel_kyiv')]"),

    # 18. Ссылка YouTube по href
    ("YouTube link", "//div[@id='contactsSection']//a[contains(@href, 'youtube.com/user/HillelITSchool')]"),

    # 19. Ссылка Instagram по href
    ("Instagram link", "//div[@id='contactsSection']//a[contains(@href, 'instagram.com/hillel_itschool')]"),

    # 20. Ссылка LinkedIn по href
    ("LinkedIn link", "//div[@id='contactsSection']//a[contains(@href, 'linkedin.com/school/ithillel')]"),

    # 21. Footer по классу
    ("Footer", "//footer[contains(@class, 'footer')]"),

    # 22. Header по классу
    ("Header", "//header[contains(@class, 'header')]"),

    # 23. Ссылка Home по тексту
    ("Home navigation link", "//header//a[normalize-space(text())='Home']"),

    # 24. Ссылка About по тексту
    ("About navigation link", "//header//a[normalize-space(text())='About']"),

    # 25. Ссылка Contacts по тексту
    ("Contacts navigation link", "//header//a[normalize-space(text())='Contacts']"),
]

CSS_LOCATORS = [
    # 1. Header
    ("Header", "header.header"),

    # 2. Главная секция
    ("Hero section", "section.hero"),

    # 3. Контейнер описания
    ("Hero descriptor", ".hero-descriptor"),

    # 4. Заголовок главного экрана
    ("Hero title", "h1.hero-descriptor_title.display-2"),

    # 5. Описание главного экрана
    ("Hero description", "p.hero-descriptor_desc.lead"),

    # 6. Кнопка Sign up
    ("Sign up button", "button.hero-descriptor_btn.btn.btn-primary"),

    # 7. Контейнер видео
    ("Hero video", ".hero-video"),

    # 8. Секция About по ID
    ("About section", "#aboutSection"),

    # 9. Секция About по ID и классу
    ("About section by ID and class", "#aboutSection.section.about"),

    # 10. Контейнер внутри About
    ("About container", "#aboutSection .container"),

    # 11. Блоки About
    ("About blocks", "#aboutSection .about-block"),

    # 12. Изображение About
    ("About picture", "#aboutSection .about-block_picture.about-picture"),

    # 13. Заголовок Log fuel expenses
    ("Fuel expenses title", "#aboutSection p.about-block_title.h2"),

    # 14. Описание Log fuel expenses
    ("Fuel expenses description", "#aboutSection p.about-block_descr.lead"),

    # 15. Секция Contacts
    ("Contacts section", "#contactsSection"),

    # 16. Секция Contacts с классом
    ("Contacts section by ID and class", "#contactsSection.section.contacts"),

    # 17. Заголовок Contacts
    ("Contacts heading", "#contactsSection h2"),

    # 18. Контейнер социальных сетей
    ("Social links container", "#contactsSection .contacts_socials.socials"),

    # 19. Все ссылки социальных сетей
    ("Social links", "#contactsSection a.socials_link"),

    # 20. Facebook по атрибуту href
    ("Facebook link", "#contactsSection a.socials_link[href*='facebook.com']"),

    # 21. Telegram по атрибуту href
    ("Telegram link", "#contactsSection a.socials_link[href*='t.me/ithillel_kyiv']"),

    # 22. YouTube по атрибуту href
    ("YouTube link", "#contactsSection a.socials_link[href*='youtube.com/user/HillelITSchool']"),

    # 23. Instagram по атрибуту href
    ("Instagram link", "#contactsSection a.socials_link[href*='instagram.com/hillel_itschool']"),

    # 24. LinkedIn по атрибуту href
    ("LinkedIn link", "#contactsSection a.socials_link[href*='linkedin.com/school/ithillel']"),

    # 25. Footer
    ("Footer", "footer.footer"),
]


if __name__ == "__main__":
    print(f"XPath locators: {len(XPATH_LOCATORS)}")
    print(f"CSS locators: {len(CSS_LOCATORS)}")
