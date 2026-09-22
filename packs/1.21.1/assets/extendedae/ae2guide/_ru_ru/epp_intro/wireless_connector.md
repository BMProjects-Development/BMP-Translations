---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: Беспроводной соединитель МЭ
    icon: extendedae:wireless_connect
categories:
- расширенные устройства
item_ids:
- extendedae:wireless_connect
- extendedae:wireless_tool
---

# Беспроводной соединитель МЭ

<Row gap="20">
<BlockImage id="extendedae:wireless_connect" scale="6"></BlockImage>
<ItemImage id="extendedae:wireless_tool" scale="6"></ItemImage>
</Row>

Беспроводной соединитель МЭ может соединять две сети, как <ItemLink id="ae2:quantum_link" />, но с ограниченными расстояниями и не может
пересекать измерения. Беспроводной соединитель МЭ поддерживает только соединения "один к одному", вам нужно использовать <ItemLink id="extendedae:wireless_hub" />,
если вы хотите соединения "многие ко многим".

## Соединение беспроводных соединителей

Нажмите на два беспроводных соединителя, которые вы хотите соединить, с помощью Набора для настройки беспроводной сети МЭ, после чего вы сможете соединить их вместе.

Крадучись + Нажмите, чтобы сбросить текущие настройки Набора для настройки беспроводной сети МЭ.

Беспроводной соединитель МЭ изменит свою текстуру, когда соединение будет успешно установлено.

Несоединенные беспроводные соединители МЭ

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_off.snbt"></ImportStructure>
</GameScene>

Соединенные беспроводные соединители МЭ

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_on.snbt"></ImportStructure>
</GameScene>

## Цвет

Беспроводные соединители могут быть окрашены как кабели и соединяют только кабель/соединители того же цвета.

Вам понадобится <ItemLink id="ae2:color_applicator" />, чтобы окрасить соединитель.

Таким образом, вы можете настроить свои беспроводные соединители следующим образом:

<GameScene zoom="3" background="transparent" interactive={true}>
  <ImportStructure src="../structure/wireless_connector_setup.snbt"></ImportStructure>
</GameScene>

## Потребление энергии

Беспроводной соединитель МЭ потребляет больше энергии, когда они находятся дальше друг от друга. Его кривая зависимости стоимости от расстояния нелинейна, поэтому потребление
энергии может стать очень высоким, если они находятся слишком далеко друг от друга.

Вы можете использовать <ItemLink id="ae2:energy_card" /> для экономии энергии, каждая карта может снизить затраты энергии на 10%.

---
