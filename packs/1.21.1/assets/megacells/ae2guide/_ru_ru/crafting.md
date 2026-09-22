---
navigation:
  title: MEGA Авто-крафт
  icon: 256m_crafting_storage
  parent: index.md
  position: 020
categories:
  - megacells
item_ids:
  - mega_crafting_unit
  - 1m_crafting_storage
  - 4m_crafting_storage
  - 16m_crafting_storage
  - 64m_crafting_storage
  - 256m_crafting_storage
  - mega_crafting_accelerator
  - mega_crafting_monitor
  - mega_pattern_provider
  - cable_mega_pattern_provider
---

# MEGA Ячейки: Авто-крафт

<GameScene zoom="6" background="transparent">
  <ImportStructure src="assets/assemblies/crafting_cpu.snbt" />
  <IsometricCamera yaw="195" pitch="10" />
</GameScene>

## MEGA [Процессоры Крафта](ae2:items-blocks-machines/crafting_cpu_multiblock.md)

<Row>
  <BlockImage id="mega_crafting_unit" scale="4" />
  <BlockImage id="1m_crafting_storage" scale="4" />
  <BlockImage id="4m_crafting_storage" scale="4" />
  <BlockImage id="16m_crafting_storage" scale="4" />
  <BlockImage id="64m_crafting_storage" scale="4" />
  <BlockImage id="256m_crafting_storage" scale="4" />
</Row>

Как и в случае с ячейками хранения, MEGA также предлагает свои более крупные уровни хранения для процессоров крафта. Хотя они также требуют своей собственной специализированной версии <ItemLink id="ae2:crafting_unit" />, чтобы приспособиться к увеличению их мощности, они все равно легко справятся даже с самыми большими задачами крафта благодаря большему объему памяти, а также будут выглядеть *чертовски круто* в черном цвете.

<RecipeFor id="mega_crafting_unit" />
<RecipeFor id="1m_crafting_storage" />
<RecipeFor id="4m_crafting_storage" />
<RecipeFor id="16m_crafting_storage" />
<RecipeFor id="64m_crafting_storage" />
<RecipeFor id="256m_crafting_storage" />

В качестве дополнительного бонуса, MEGA также предлагает свой эквивалент <ItemLink id="ae2:crafting_accelerator" />, но с преимуществом предоставления не одного, а *ЧЕТЫРЕХ* сопроцессорных потоков на месте каждого отдельного добавленного сопроцессорного блока.

<BlockImage id="mega_crafting_accelerator" scale="4" />
<RecipeFor id="mega_crafting_accelerator" />

И просто для полноты комплекта, также существует MEGA эквивалент <ItemLink id="ae2:crafting_monitor" />. Он на самом деле ничем не отличается от обычного монитора, но служит дополнением к вышеупомянутым блокам для пользователей, желающих сохранить эстетическую согласованность и тот же гладкий, темный вид по всему своему мультиблоку CPU.

<BlockImage id="mega_crafting_monitor" scale="4" />
<RecipeFor id="mega_crafting_monitor" />

## MEGA Поставщик Шаблонов

<Row>
  <BlockImage id="mega_pattern_provider" scale="4" />
  <GameScene zoom="4" background="transparent">
    <ImportStructure src="assets/assemblies/cable_mega_pattern_provider.snbt" />
  </GameScene>
</Row>

Служа дополнением к <ItemLink id="ae2:pattern_provider" />, **MEGA Поставщик Шаблонов** продолжает тенденцию предоставления более крупных вариантов соответствующих устройств AE2, удваивая емкость шаблонов, что позволяет хранить и обрабатывать в общей сложности 18 шаблонов. Однако это сопряжено с компромиссом: он может хранить только [**шаблоны обработки**](ae2:items-blocks-machines/patterns.md), поэтому он не будет работать с <ItemLink id="ae2:molecular_assembler" />.

<Row>
  <RecipeFor id="mega_pattern_provider" />
  <RecipeFor id="cable_mega_pattern_provider" />
</Row>