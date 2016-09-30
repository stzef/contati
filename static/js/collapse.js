
    si (this.options.parent) {
      esto. $ parent = $ (this.options.parent)
    }

    this.options.toggle && this.toggle ()
  }

  Collapse.prototype = {

    constructor: Reducir

  , Dimensión: function () {
      var = hasWidth esto. element.hasClass $ ( "ancho")
      volver hasWidth? 'Width': 'altura'
    }

  , Espectáculo: function () {
      var dimensión
        , desplazamiento
        , sustancias activas
        , HasData

      si el retorno (this.transitioning)

      dimensión = this.dimension ()
      desplazarse = $ .camelCase ([ 'scroll', dimensión] .join ( '-'))
      = activos esto. $ && padres esto. parent.find $ ( '> .accordion-grupo> .en')

      si (activos && actives.length) {
        HasData = actives.data ( "colapso")
        si el retorno (HasData && hasData.transitioning)
        actives.collapse ( 'ocultar')
        HasData || actives.data ( 'colapso', null)
      }

      esto. $ elemento [dimensión] (0)
      this.transition ( 'addClass', $ .Los ( 'show'), 'muestra')
      esto. $ elemento [dimensión] (esto. $ elemento [0] [desplazamiento])
    }

  , Ocultar: function () {
      var dimensión
      si el retorno (this.transitioning)
      dimensión = this.dimension ()
      this.reset (esto. $ elemento [dimensión] ())
      this.transition ( 'removeClass', $ .Los ( 'ocultar'), 'oculto')
      esto. $ elemento [dimensión] (0)
    }

  , Restablecer: function (tamaño) {
      dimensión var = this.dimension ()

      esto. elemento $
        .removeClass ( "colapso")
        [Dimensión] (tamaño || 'auto')
        [0] .offsetWidth

      esto. $ elemento [tamaño! == null? 'AddClass': 'removeClass'] ( "colapso")

      devolver este
    }

  , La transición: la función (método, StartEvent, completeEvent) {
      var que este =
        , Completa = function () {
            si ( 'show' startEvent.type ==) that.reset ()
            that.transitioning = 0
            que. $ element.trigger (completeEvent)
          }

      esto. $ element.trigger (StartEvent)

      si el retorno (startEvent.isDefaultPrevented ())

      this.transitioning = 1

      esto. $ elemento [método] ( "en")

      $ && .support.transition Esto. Element.hasClass $ ( 'colapso')?
        . $ Element.one este (. $ Support.transition.end, completa):
        completar()
    }

  , Alternar: function () {
      esta [esto. element.hasClass $ ( 'en')? 'ocultar mostrar']()
    }

  }


 / * COLAPSABLE PLUGIN DEFINICIÓN
  * * ============================== /

  $ .fn.collapse = Function (opcional) {
    volver this.each (function () {
      var $ this = $ (this)
        , Datos = $ this.data ( "colapso")
        , Opciones = opción typeof opción == 'objeto' &&
      if (! datos) $ this.data ( "colapso", (datos = new Cerrar (esto, las opciones)))
      si (typeof opción == 'cadena') de datos [opción] ()
    })
  }

  $ .fn.collapse.defaults = {
    basculante: true
  }

  $ .fn.collapse.Constructor = Cerrar


 / * COLAPSABLE DATOS-API
  * * ==================== /

  $ (Function () {
    $ ( "Cuerpo"). En ( 'click.collapse.data-api', '[datos de palanca = colapso]', function (e) {
      var $ this = $ (este), href
        , Target = $ this.attr ( 'data-target')
          || e.preventDefault ()
          || (Href = $ this.attr ( 'href')) && href.replace (/.* (? = # [^ \ S] + $) / '') // tira para IE7
        , Opción = $ (objetivo) .data ( "colapso")? 'Alternar': $ this.data ()
      $ (Objetivo) .collapse (opcional)
    })
  })

} (Window.jQuery);