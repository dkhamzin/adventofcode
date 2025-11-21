$inputs = Get-Content .\01\input.txt


$position = 0
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
}

$position