.data
string1_1: .asciiz "Enter a number:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "fib("
string3_2: .asciiz ")\t= "
string3_3: .asciiz ";\n\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -24
        sw      $fp, 24($sp)
        move    $fp, $sp
        sw      $4, 8($fp)
        # BEGIN IF CONDITION
        lw      $8, 8($fp)
        slti    $8, $8, 2
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        nop     
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        lw      $8, 8($fp)
        subi    $8, $8, 1
        sw      $8, 16($fp)
        lw      $4, 16($fp)
        jal     f
        lw      $8, 8($fp)
        subi    $8, $8, 2
        sw      $8, 20($fp)
        lw      $4, 20($fp)
        jal     f
        add     $8, $11, $14
        nop     
        # END ELSE BODY
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 24($sp)
        addiu   $sp, $sp, 28
        jr      $ra
                
main:   
        addiu   $sp, $sp, -52
        sw      $fp, 52($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 32($fp)
        addiu   $8, $fp, 32
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $8, 40($fp)
        lw      $4, 40($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 32($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        li      $8, 1
        sw      $8, 44($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $8, 44($fp)
        lw      $9, 32($fp)
        sle     $8, $8, $9
        beq     $8, $0, $L3
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $8, 44($fp)
        addi    $8, $8, 1
        sw      $8, 48($fp)
        lw      $8, 48($fp)
        sw      $8, 44($fp)
        lw      $4, 44($fp)
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 44($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
                
        li      $v0, 1
        syscall 
        la      $4, string3_3
        li      $v0, 4
        syscall 
        j       $L2
        # END WHILE BODY
                
$L3:    
        nop     
        move    $sp, $fp
        lw      $fp, 52($sp)
        addiu   $sp, $sp, 56
        li      $v0, 10
        syscall 