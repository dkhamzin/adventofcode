$inputs = Get-Content .\03\input.txt

$coords = [System.Management.Automation.Host.coordinates]::new(0, 0)
$coordHash = @{$coords.ToString() = 0 }

foreach ($char in [char[]]$inputs)
{
    if ($char -eq '>')
    {
        $coords.X++
    }

    if ($char -eq '<')
    {
        $coords.X--
    }

    if ($char -eq '^')
    {
        $coords.Y++
    }

    if ($char -eq 'v')
    {
        $coords.Y--
    }

    $coordHash.($coords.ToString()) = 0
}

$coordHash.Count