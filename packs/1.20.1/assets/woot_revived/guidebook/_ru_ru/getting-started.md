---
navigation:
  title: "Начало работы"
  position: 10
  icon: "woot_revived:stygian_ingot"
---
# Начало работы

## Получение стигийского слитка

Чтобы начать работу с Woot Revived, сначала вам нужно создать немного <ItemImage id="stygian_dust" scale="0.5"/> Стигийской пыли.
<Recipe id="stygian_dust" />

Затем вам нужно будет переплавить её, чтобы получить <ItemImage id="stygian_ingot" scale="0.5"/> Стигийский слиток.
<Recipe id="stygian_ingot_cook" />

## Получение форм

Сначала вам нужно сделать <ItemImage id="stygian_anvil" scale="0.5"/> Стигийскую наковальню и <ItemImage id="stygian_hammer" scale="0.5"/> Стигийский молот.
<Row>
<Recipe id="stygian_anvil" />
<Recipe id="stygian_hammer" />
</Row>

Затем вам нужно будет поставить Стигийскую наковальню на <ItemImage id="minecraft:magma_block" scale="0.5"/> Блок магмы.

Чтобы создавать предметы на Стигийской наковальне, вам нужно нажимать по ней ПКМ Стигийским молотом.

Для каждой формы вам понадобится <ItemImage id="minecraft:quartz" scale="0.5"/> Кварц и <ItemImage id="stygian_ingot" scale="0.5"/> Стигийский слиток.

Обратите внимание, что формы не расходуются при крафте, вам нужна всего одна штука каждого вида.

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/plate_mold.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="plate_mold" scale="2"/>
  Для создания формы для пластины вам понадобится <ItemImage id="minecraft:iron_trapdoor" scale="0.5"/> Железный люк.
</Row>

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/shard_mold.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="shard_mold" scale="2"/>
  Для создания формы для осколка вам понадобится <ItemImage id="minecraft:prismarine_shard" scale="0.5"/> Осколок призмарина.
</Row>

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/dye_casing_mold.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="dye_casing_mold" scale="2"/>
  Для создания формы для корпуса красителя вам понадобится <ItemImage id="minecraft:white_dye" scale="0.5"/> любой краситель.
</Row>

## Создание основания фабрики

Для создания всех блоков мода вам нужно будет скрафтить Основание фабрики.

Сначала вам понадобится <ItemImage id="stygian_plate" scale="0.5"/> Стигийская пластина.

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/stygian_plate.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="stygian_plate" scale="2"/>
  Для её создания вам нужна <ItemImage id="plate_mold" scale="0.5"/> форма для пластины и <ItemImage id="stygian_ingot" scale="0.5"/> Стигийский слиток.
</Row>

После этого вы сможете скрафтить блок Основания фабрики.

<Recipe id="factory_base" />

## А что потом?

Теперь вы можете начать [захватывать мобов](mob-shard.md), или же приступить к [постройке своей первой фабрики](factory/copper.md)!