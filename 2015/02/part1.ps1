$inputs = Get-Content .\02\input.txt

$totalArea = 0
$inputs | ForEach-Object {
    $dimenstions = $_ -split 'x'

    $l = [int]$dimenstions[0]
    $w = [int]$dimenstions[1]
    $h = [int]$dimenstions[2]

    $area = 2 * $l * $w + 2 * $w * $h + 2 * $h * $l

    $sortedDimensions =  ($l, $w, $h) | Sort-Object { $_ }
    $wrap = $sortedDimensions[0] * $sortedDimensions[1]
    $totalArea += ($area + $wrap)
}

$totalArea