---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоблокировка излучателя уровня
  icon: level_emitter
---

# Автоблокировка излучателя уровня

Может возникнуть вопрос: "Как поддерживать определенное количество предмета на складе, создавая его по мере необходимости?".

Одним из решений является использование <ItemLink id="export_bus" />, <ItemLink id="level_emitter" /> и <ItemLink id="crafting_card" /> для автоматического запроса новых предметов
из [автокрафта](../ae2-mechanics/autocrafting.md) вашей сети. Эта настройка предназначена для поддержания большого количества одного предмета.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (1) Шина экспорта: Фильтруется до нужного предмета. Имеет карту красного камня и карту крафта. Режим работы с красным камнем установлен на
        "Активен при наличии сигнала", режим крафта установлен на "Не использовать запасы предметов".
        <Row><ItemImage id="redstone_card" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
        (2) Излучатель уровня: Настраивается на нужный элемент и количество, устанавливается на "Излучать, когда уровень ниже предела".
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (3) Интерфейс: В конфигурации по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* В <ItemLink id="export_bus" /> (1) происходит фильтрация на нужный предмет. Он имеет <ItemLink id="redstone_card" /> и <ItemLink id="crafting_card" />.
Режим " Красного камня" установлен на "Активный с сигналом", "Поведение при крафте" установлено на "Не использовать запасы предметов".
* <ItemLink id="level_emitter" /> (2) настроен на нужный предмет и его количество и установлен на "Излучать, когда уровень ниже предела".
* <ItemLink id="interface" /> (3) имеет конфигурацию по умолчанию.

## Как это работает

1. Если количество нужного элемента в [хранилищи сети](../ae2-mechanics/import-export-storage.md) ниже количества, указанного в параметре
   <ItemLink id="level_emitter" />, он издаст сигнал красного камня.
2. После получения сигнала красного камня (и благодаря тому, что <ItemLink id="crafting_card" /> настроен на неиспользование запасов),
   <ItemLink id="export_bus" /> запросит у сетевой системы [автокрафта](../ae2-mechanics/autocrafting.md) создание 
большего количества нужного предмета, а затем экспортирует его.
3. После того как в него будет помещен предмет (и при этом он не будет иметь ничего в своем внутреннем инвентаре), <ItemLink id="interface" /> поместит этот предмет в сетевое хранилище.