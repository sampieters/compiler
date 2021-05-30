.data
float1: .float 5.000000e-01
string1_1: .asciiz ""
string1_2: .asciiz "; "
string1_3: .asciiz "; "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -24
        sw      $fp, 20($sp)
        sw      $ra, 16($sp)
        sw      $4, 12($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        l.s     $f4, float1
        s.s     $f4, 4($fp)
        li      $8, 99
        sb      $8, 8($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        l.s     $f12, 4($fp)
        li      $2, 2
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        lb      $4, 8($fp)
        li      $2, 11
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 0
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 12($sp)
        lw      $ra, 16($sp)
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $2, 10
        syscall 