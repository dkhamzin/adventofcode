$inputs = Get-Content .\01\input.txt


$position = 0
$step = 1
foreach ($char in [char[]]$inputs)
{
    if ($char -eq '(')
    {
        $position++
    }
    else
    {
        $position--
    }

    if ($position -eq -1)
    {
        return $step
    }
    $step++
}
