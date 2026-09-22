---
navigation:
  parent: example-setups/example-setups-index.md
  title: Автоматизация зарядника
  icon: charger
---

# Автоматизация зарядника

Автоматизация <ItemLink id="charger" /> достаточно проста. С помощью <ItemLink id="pattern_provider" /> ингредиент помещается в зарядное устройство, затем с помощью [труб подсетей](pipe-subnet.md)
или другой элемент-труба возвращает результат в интерфейс.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/charger_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Поставщик шаблонов: В конфигурации по умолчанию, с соответствующими схемами обработки. Также обеспечивает питание зарядника.

        ![Шаблон зарядки](../assets/diagrams/charger_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="1 1.3 1">
        (2) Шина импорта: В конфигурации по умолчанию.
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (3) Шина хранения: В конфигурации по умолчанию.
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        К основной сети
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Конфигурации

* <ItemLink id="pattern_provider" /> (1) находится в конфигурации по умолчанию, с соответствующими <ItemLink id="processing_pattern" />.
  Он также обеспечивает <ItemLink id="charger" /> [энергией](../ae2-mechanics/energy.md), поскольку действует как [кабель](../items-blocks-machines/cables.md).
  
    ![Charger Pattern](../assets/diagrams/charger_pattern.png)

* <ItemLink id="import_bus" /> (2) находится в конфигурации по умолчанию.
* <ItemLink id="storage_bus" /> (3) имеет конфигурацию по умолчанию.

## Как это работает

1. Блок <ItemLink id="pattern_provider" /> помещает ингредиенты в блок <ItemLink id="charger" />.
2. Зарядник производит зарядку.
3. Устройство <ItemLink id="import_bus" /> в зеленой подсети извлекает результат из зарядника и пытается сохранить его в
   [хранилище сети](../ae2-mechanics/import-export-storage.md).
4. Единственным хранилищем в зеленой подсети является <ItemLink id="storage_bus" />, которое хранит полученные элементы в интерфейсе, возвращая их в основную сеть.
