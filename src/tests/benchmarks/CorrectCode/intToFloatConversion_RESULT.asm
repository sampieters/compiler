.data
float1: .float 1.500000e+00
string1_1: .asciiz ""
string1_2: .asciiz " "
string1_3: .asciiz " "
string1_4: .asciiz "\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 24($sp)
        sw      $ra, 20($sp)
        sw      $4, 16($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        lw      $8, 0($fp)
        sw      $8, 4($fp)
        l.s     $f4, 4($fp)
        cvt.s.w $f5,$f4
        s.s     $f5, 8($fp)
        l.s     $f6, float1
        s.s     $f6, 12($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        l.s     $f12, 8($fp)
        li      $2, 2
        syscall 
        la      $4, string1_3
        li      $2, 4
        syscall 
        l.s     $f12, 12($fp)
        li      $2, 2
        syscall 
        la      $4, string1_4
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 16($sp)
        lw      $ra, 20($sp)
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 