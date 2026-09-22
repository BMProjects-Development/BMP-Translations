---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Молекулярный сборщик
  icon: molecular_assembler
  position: 310
categories:
- machines
item_ids:
- ae2:molecular_assembler
---

# Молекулярный сборщик

<BlockImage id="molecular_assembler" scale="8" />

Молекулярный сборщик принимает введенные в него элементы и выполняет операцию, заданную соседним <ItemLink id="pattern_provider" />,
или вставленным <ItemLink id="crafting_pattern" />, <ItemLink id="smithing_table_pattern" />, или <ItemLink id="stonecutting_pattern" />,
затем помещает результат в соседние инвентари.

У этого сборщика есть схема крафта, в которой указан рецепт 1 дубовое бревно = 4 дубовые доски. Когда дубовые бревна подаются в верхнюю воронку,
сборщик изготавливает дубовые доски и выплевывает их в нижнюю воронку.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Основное использование молекулярного сборщика

Однако основное их применение - рядом с <ItemLink id="pattern_provider" />. В этом случае интерфейсы ведут себя особым образом,
и будут передавать информацию о соответствующем шаблоне вместе с ингредиентами соседним сборщикам. Поскольку сборщики автоматически выбрасывают результаты
крафта в соседние инвентари (и, соответственно, в слоты возврата МЭ интерфейса), то для автоматизации работы сборщика на интерфейсе этого достаточно.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Модернизации

Молекулярный сборщик поддерживает следующие [улучшения](upgrade_cards.md):

*   <ItemLink id="speed_card" />

## Рецепты

<RecipeFor id="molecular_assembler" />

## Примечание

Optifine нарушает функцию "подталкивания к соседним инвентарям", поэтому большинство крафтовых установок с использованием сборщиков работать не будут.