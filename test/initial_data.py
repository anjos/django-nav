[
  {
    "pk": 1, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Professional Website", 
      "language": "en", 
      "url": "http://andreanjos.org/", 
      "image": "", 
      "image_width": 16, 
      "sites": [
        1
      ], 
      "priority": 0, 
      "image_height": 16, 
      "image_url": "http://andreanjos.org/media/favicon.ico", 
      "user": "X", 
      "groups": [], 
      "description": "A link to my professional website"
    }
  }, 
  {
    "pk": 2, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Google", 
      "language": "en", 
      "url": "http://www.google.com/", 
      "image": "", 
      "image_width": 16, 
      "sites": [
        1
      ], 
      "priority": 5, 
      "image_height": 16, 
      "image_url": "http://www.google.com/favicon.ico", 
      "user": "X", 
      "groups": [], 
      "description": "Visit the Google Website"
    }
  }, 
  {
    "pk": 3, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Login", 
      "language": "en", 
      "url": "/login/?next={{ full_path }}", 
      "image": "menus/2010/04/go-next.png", 
      "image_width": 16, 
      "sites": [], 
      "priority": 10, 
      "image_height": 16, 
      "image_url": "", 
      "user": "N", 
      "groups": [], 
      "description": "Login to this website"
    }
  }, 
  {
    "pk": 4, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Logout", 
      "language": "en", 
      "url": "/logout/?next={{ full_path }}", 
      "image": "menus/2010/04/16x16/system-log-out_.png", 
      "image_width": 16, 
      "sites": [
        1
      ], 
      "priority": 10, 
      "image_height": 16, 
      "image_url": "", 
      "user": "L", 
      "groups": [], 
      "description": "Logout from this website"
    }
  }, 
  {
    "pk": 5, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Test group", 
      "language": "en", 
      "url": "{% url media \"\" %}", 
      "image": "", 
      "image_width": null, 
      "sites": [
        1
      ], 
      "priority": 5, 
      "image_height": null, 
      "image_url": "", 
      "user": "G", 
      "groups": [
        1
      ], 
      "description": "Only shows to a subgroup of people"
    }
  }, 
  {
    "pk": 6, 
    "model": "nav.item", 
    "fields": {
      "parent": null, 
      "name": "Administration Panel", 
      "language": "en", 
      "url": "{% url admin:index %}", 
      "image": "", 
      "image_width": null, 
      "sites": [
        1
      ], 
      "priority": 5, 
      "image_height": null, 
      "image_url": "", 
      "user": "S", 
      "groups": [], 
      "description": "Click here to access our administration panel"
    }
  }, 
  {
    "pk": 1, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 1, 
      "name": "Website Profissional", 
      "language": "pt-br", 
      "description": "Um link para o meu site profissional"
    }
  }, 
  {
    "pk": 2, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 2, 
      "name": "Google", 
      "language": "pt-br", 
      "description": "Visite o site Google"
    }
  }, 
  {
    "pk": 3, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 3, 
      "name": "Conex\u00e3o", 
      "language": "pt-br", 
      "description": "Fazer conex\u00e3o a este website"
    }
  }, 
  {
    "pk": 4, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 4, 
      "name": "Desconectar", 
      "language": "pt-br", 
      "description": "Desconectar deste website"
    }
  }, 
  {
    "pk": 5, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 6, 
      "name": "Painel de Administra\u00e7\u00e3o", 
      "language": "pt-br", 
      "description": "Clique aqui para acessar nosso painel de administra\u00e7\u00e3o"
    }
  }, 
  {
    "pk": 6, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 5, 
      "name": "Grupo de teste", 
      "language": "pt-br", 
      "description": "Somente \u00e9 mostrado a um subgrupo de pessoas"
    }
  }, 
  {
    "pk": 7, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 1, 
      "name": "Site Web Professionnel", 
      "language": "fr", 
      "description": "Un lien vers mon site professionnel"
    }
  }, 
  {
    "pk": 8, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 1, 
      "name": "Sitio Web Profesional", 
      "language": "es", 
      "description": "Un enlace a mi sitio web profesional"
    }
  }, 
  {
    "pk": 9, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 2, 
      "name": "Google", 
      "language": "fr", 
      "description": "Visitez le site Web de Google"
    }
  }, 
  {
    "pk": 10, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 2, 
      "name": "Google", 
      "language": "es", 
      "description": "Visite el sitio web Google"
    }
  }, 
  {
    "pk": 11, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 5, 
      "name": "Ensemble de teste", 
      "language": "fr", 
      "description": "Elle n'appara\u00eet que pour un sous-ensemble de la population"
    }
  }, 
  {
    "pk": 12, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 5, 
      "name": "Grupo de prueba", 
      "language": "es", 
      "description": "S\u00f3lo se muestra a un subconjunto de personas"
    }
  }, 
  {
    "pk": 13, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 6, 
      "name": "Panneau d'Administration", 
      "language": "fr", 
      "description": "Cliquez ici pour acc\u00e9der notre paneau d'adminstration"
    }
  }, 
  {
    "pk": 14, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 6, 
      "name": "Panel de Administraci\u00f3n", 
      "language": "es", 
      "description": "Haga clic aqu\u00ed para acceder al panel de administraci\u00f3n"
    }
  }, 
  {
    "pk": 15, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 3, 
      "name": "Connexion", 
      "language": "fr", 
      "description": "Se connecter a ce site web"
    }
  }, 
  {
    "pk": 16, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 3, 
      "name": "Conexi\u00f3n", 
      "language": "es", 
      "description": "Haga la conexi\u00f3n a este sitio web"
    }
  }, 
  {
    "pk": 17, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 4, 
      "name": "D\u00e9connecter", 
      "language": "fr", 
      "description": "Deconnectez de ce site web"
    }
  }, 
  {
    "pk": 18, 
    "model": "nav.itemtranslation", 
    "fields": {
      "item": 4, 
      "name": "Desconectar", 
      "language": "es", 
      "description": "Desconecte de este sitio web"
    }
  }
]
