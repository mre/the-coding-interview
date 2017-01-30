<?php
declare(strict_types=1);

class CashUnits {

    private static $cashUnits = [
        500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
    ];

    public function countCashUnits(float $input) : array {
        $cashUnitCounts = [];
        foreach (static::$cashUnits as $cashUnit) {
            $cashUnitCounts[(string) $cashUnit] = (int) floor($input / $cashUnit);
            $input = round(fmod($input, $cashUnit), 2);
        }
        return $cashUnitCounts;
    }

}

$input = 1972.78;
$result = (new CashUnits())->countCashUnits($input);

assert($result['500'] === 3);
assert($result['200'] === 2);
assert($result['100'] === 0);
assert($result['50'] === 1);
assert($result['20'] === 1);
assert($result['10'] === 0);
assert($result['5'] === 0);
assert($result['2'] === 1);
assert($result['1'] === 0);
assert($result['0.5'] === 1);
assert($result['0.2'] === 1);
assert($result['0.1'] === 0);
assert($result['0.05'] === 1);
assert($result['0.02'] === 1);
assert($result['0.01'] === 1);
