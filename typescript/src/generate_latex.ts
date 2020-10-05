import { monsterToLatex } from "@src/latex/monster_to_latex";
import { monstersByType } from "@src/monsters";
import { MonsterType, monsterTypes, typeDescriptions } from "@src/monsters/types";
import { titleCase } from "change-case";
import cli from "commander";
import fs from "fs";
import _ from "lodash";

function formatPluralMonsterType(monsterType: MonsterType): string {
  if (["planeforged", "undead"].includes(monsterType)) {
    return monsterType;
  } else {
    return `${monsterType}s`;
  }
}

function generateLatex(latexType: string): string {
  let latex = "";
  if (latexType === "monsters") {
    for (const monsterType of monsterTypes) {
      const pluralText = formatPluralMonsterType(monsterType);
      latex += `
        \\newpage
        \\section{${titleCase(pluralText)}}

        All ${pluralText} have the following properties unless noted otherwise in their description:
        ${typeDescriptions[monsterType]}
      `;
      for (const monster of monstersByType[monsterType]) {
        latex += monsterToLatex(monster);
      }
    }
  }
  return latex;
}

function main(latexType: string, outputFilename?: string) {
  const latex = generateLatex(latexType);
  if (outputFilename) {
    fs.writeFileSync(outputFilename, latex);
  } else {
    console.log(latex);
  }
}

if (require.main === module) {
  cli
    .option("-o, --output <outputFilename>")
    .option("-t, --type <latexType>")
    .parse(process.argv);
  if (!cli.type) {
    throw new Error("Must provide --type");
  }
  main(cli.type, cli.output);
}
