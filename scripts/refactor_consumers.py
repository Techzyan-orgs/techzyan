# 1. Update src/app/contact/page.tsx
with open('src/app/contact/page.tsx', 'r', encoding='utf-8') as f:
    contact_content = f.read()

contact_content = contact_content.replace(
    "window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');",
    "window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');"
)
contact_content = contact_content.replace(
    "<span>Kolkata, West Bengal, India</span>",
    "<span>{siteConfig.location.fullAddress}</span>"
)
with open('src/app/contact/page.tsx', 'w', encoding='utf-8') as f:
    f.write(contact_content)
print("Updated src/app/contact/page.tsx")

# 2. Update src/components/ConsultationModal.tsx
with open('src/components/ConsultationModal.tsx', 'r', encoding='utf-8') as f:
    consult_content = f.read()

consult_content = consult_content.replace(
    "window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');",
    "window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');"
)
with open('src/components/ConsultationModal.tsx', 'w', encoding='utf-8') as f:
    f.write(consult_content)
print("Updated src/components/ConsultationModal.tsx")

# 3. Update src/components/PujaConsultationModal.tsx
with open('src/components/PujaConsultationModal.tsx', 'r', encoding='utf-8') as f:
    puja_content = f.read()

puja_content = puja_content.replace(
    "window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');",
    "window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');"
)
with open('src/components/PujaConsultationModal.tsx', 'w', encoding='utf-8') as f:
    f.write(puja_content)
print("Updated src/components/PujaConsultationModal.tsx")

# 4. Update src/components/Footer.tsx
with open('src/components/Footer.tsx', 'r', encoding='utf-8') as f:
    footer_content = f.read()

footer_content = footer_content.replace(
    "<span>Kolkata, West Bengal, India</span>",
    "<span>{siteConfig.location.fullAddress}</span>"
)
footer_content = footer_content.replace(
    "Techzyan Technical Studio",
    "{siteConfig.legalName}"
)
with open('src/components/Footer.tsx', 'w', encoding='utf-8') as f:
    f.write(footer_content)
print("Updated src/components/Footer.tsx")
