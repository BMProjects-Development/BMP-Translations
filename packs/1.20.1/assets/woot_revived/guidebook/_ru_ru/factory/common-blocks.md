---
navigation:
  parent: factory/factory-index.md
  title: "Общие блоки"
  icon: "woot_revived:factory_connect"
  position: 0
---
# Общие блоки

У каждой фабрики есть общая схема с этими блоками. Чтобы узнать подробности о их размещении, перейдите на страницы уровней.

## Сердце фабрики

<ItemImage id="heart" scale="0.5"/> [Сердце фабрики](../machines-blocks/heart.md) — это главный контроллер вашей фабрики.

<RecipeFor id="heart" />

## Слот для улучшений

В <ItemImage id="factory_upgrade" scale="0.5"/> [Слоте для улучшений](../machines-blocks/upgrade-slot.md) хранятся модули улучшений вашей фабрики.

<RecipeFor id="factory_upgrade" />

## Фальшивый рассадник

В <ItemImage id="fake_spawner" scale="0.5"/> [Фальшивом рассаднике](../mob-shard.md) хранится моб, который будет симулироваться.

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="../assets/anvil/fake_spawner.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="fake_spawner" scale="2"/>
  Для его создания вам понадобится запрограммированный <ItemImage id="mob_shard" scale="0.5"/> Осколок моба, <ItemImage id="prism" scale="0.5"/> Призма и <ItemImage id="factory_base" scale="0.5"/> Основание фабрики.
</Row>

## Основная база и Вторичная база

<ItemImage id="factory_ctr_base_pri" scale="0.5"/> Основная база и <ItemImage id="factory_ctr_base_sec" scale="0.5"/> Вторичная база являются фундаментом для вашего <ItemImage id="fake_spawner" scale="0.5"/> Фальшивого рассадника.

Обратите внимание, что фальшивые рассадники на вторичных базах не обязательны.

<Row>
  <RecipeFor id="factory_ctr_base_pri" />
  <RecipeFor id="factory_ctr_base_sec" />
</Row>

## Коннектор фабрики

<ItemImage id="factory_ctr_base_pri" scale="0.5"/> Коннектор фабрики подключает ингредиенты к вашей фабрике.

<RecipeFor id="factory_connect" />

## Импортер ингредиентов

<ItemImage id="import" scale="0.5"/> [Импортер ингредиентов](../machines-blocks/import.md) позволяет импортировать предметы или жидкости, необходимые для спавна моба.

<RecipeFor id="import" />

## Экспортер добычи

<ItemImage id="export" scale="0.5"/> [Экспортер добычи](../machines-blocks/export.md) — это место, куда будут сбрасываться все предметы или жидкости, произведенные мобами.

<RecipeFor id="export" />

## Ячейки витальности

Обратите внимание, что все ячейки витальности являются общими для всех тиров фабрики!

Используя [Схему фабрики](../machines-blocks/layout.md), вы заметите, что блок ячейки витальности циклично меняется между всеми возможными ячейками.