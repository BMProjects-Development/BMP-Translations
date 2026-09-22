---
navigation:
  parent: example-setups/example-setups-index.md
  title: Наполнитель вёдер
  icon: minecraft:water_bucket
---

# Наполнитель вёдер

См. также [опорожнитель вёдер](bucket-emptier.md).

Заметьте, что поскольку здесь используется <ItemLink id="pattern_provider" />, эта установка предназначена для интеграции в вашу систему [автосоздания](../ae2-mechanics/autocrafting.md).

Жизнь бывает неудобна, и вам нужна сама жидкость, но вы можете получить её только в ведре. Иногда механизм может сделать это за вас (например, жидкостный преобразователь из Thermal Expansion), но не всегда у вас есть мод, который сделает это удобно. К счастью, в ванильном Майнкрафте есть чуть менее удобный способ — <ItemLink id="minecraft:dispenser" />.

**Обратите внимание, что часто такая установка не требуется, так как замещение жидкостей в [терминале кодирования шаблонов](../items-blocks-machines/terminals.md#pattern-encoding-terminal) позволяет использовать саму жидкость в рецепте вместо ведра.**

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/bucket_filler.snbt" />

<BoxAnnotation color="#dddddd" min="2 1 0" max="3 2 1">
        (1) Поставщик шаблонов: настроен на блокировку создания «При наличии редстоун-сигнала», с соответствующими шаблонами обработки.

        <Row>
        ![Шаблон заполнения](../assets/diagrams/water_fill_pattern_small.png)
        ![Шаблон заполнения](../assets/diagrams/lava_fill_pattern_small.png)
        </Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1.1 0.1" max="3.2 1.9 0.9">
        (2) Интерфейс: в конфигурации по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.1 1.1 0.8" max="3.9 1.9 1">
        (3) Шина хранения №1: в конфигурации по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="4.05 1.05 0.8" max="4.95 1.95 1">
        (4) Плоскость формирования: отфильтрована на вёдра в чёрном списке с помощью карты инвертирования.
        <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.2 2 1.2" max="3.8 2.2 1.8">
        (5) Шина импортирования: отфильтрована на вёдра в чёрном списке с помощью карты инвертирования.
        <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2.1 2 0.1" max="2.9 2.2 0.9">
        (6) Шина хранения №2: в конфигурации по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="0 1.5 0.5" color="#00ff00">
        Идёт в основную сеть
    </DiamondAnnotation>

  <IsometricCamera yaw="225" pitch="45" />
</GameScene>

## Конфигурации

* <ItemLink id="pattern_provider" /> (1) настроен на блокировку создания «При наличии редстоун-сигнала», с соответствующими <ItemLink id="processing_pattern" />.

    ![Шаблон зарядного устройства](../assets/diagrams/water_fill_pattern.png)
    ![Шаблон зарядного устройства](../assets/diagrams/lava_fill_pattern.png)

* <ItemLink id="interface" /> (2) в конфигурации по умолчанию.
* Первая <ItemLink id="storage_bus" /> (3) в конфигурации по умолчанию.
* <ItemLink id="formation_plane" /> (4) отфильтрована на вёдра в чёрном списке с помощью карты инвертирования.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
* <ItemLink id="import_bus" /> (5) отфильтрована на вёдра в чёрном списке с помощью карты инвертирования.
  <Row><ItemImage id="minecraft:bucket" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
* Вторая <ItemLink id="storage_bus" /> (6) в конфигурации по умолчанию.

## Как это работает

1. <ItemLink id="pattern_provider" /> подаёт ингредиенты в <ItemLink id="interface" />. (На самом деле, для оптимизации он подаёт их напрямую через шину хранения и плоскость формирования, как будто они являются продолжением граней поставщика. Предметы никогда не попадают в интерфейс.)
2. Через механизмы, описанные в [подсетях-«трубах»](pipe-subnet.md#подача-в-несколько-мест) и <ItemLink id="formation_plane" />, ведро оказывается в <ItemLink id="minecraft:dispenser" />, а жидкость размещается плоскостью формирования.
3. <ItemLink id="minecraft:comparator" /> обнаруживает ведро в раздатчике и одновременно запитывает раздатчик и блокирует <ItemLink id="pattern_provider" />.
4. Раздатчик забирает жидкость в ведро, теперь в нём находится заполненное ведро.
5. <ItemLink id="import_bus" /> извлекает заполненное ведро из раздатчика и сохраняет его через <ItemLink id="storage_bus" /> в поставщик шаблонов, возвращая его в основную сеть.
6. Компаратор видит, что раздатчик пуст, и разблокирует поставщик.