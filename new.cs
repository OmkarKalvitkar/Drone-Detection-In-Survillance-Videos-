using System;

public class Palindrome
{
    public static void Main()
    {
        Console.Write("Enter a string: ");
        string inputString = Console.ReadLine();
        string reverseString = string.Empty;
        
        // Reversing the string
        for (int i = inputString.Length - 1; i >= 0; i--)
        {
            reverseString += inputString[i];
        }
        
        // Checking if the string is a palindrome
        if (inputString.Equals(reverseString, StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine($"{inputString} is a palindrome.");
        }
        else
        {
            Console.WriteLine($"{inputString} is not a palindrome.");
        }
    }
}
