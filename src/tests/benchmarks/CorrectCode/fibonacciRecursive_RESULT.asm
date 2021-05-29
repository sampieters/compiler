.data
string1_1: .asciiz "Enter a number:\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "fib("
string3_2: .asciiz ")\09= "
string3_3: .asciiz ";\0A\00"
.globl main
.text
                
f:      
        addiu   $sp, $sp, -4
        sw      $fp, 4($sp)
        move    $fp, $sp
        # BEGIN IF CONDITION
        lw      $8, 3($fp)
        slti    $9, $8, 2
        beq     REGISTER, $0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        nop     
        # END IF BODY
        b       $L1
        nop     
$L0:    
        # BEGIN ELSE BODY
        lw      $10, 3($fp)
        subi    $11, $10, 1
                
        jal     f
        lw      $12, 3($fp)
        subi    $13, $12, 2
                
        jal     f
        add     $14, $11, $14
        nop     
        # END ELSE BODY
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 4($sp)
        addiu   $sp, $sp, 8
        jr      $ra
                
main:   
        addiu   $sp, $sp, -20
        sw      $fp, 20($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $24, 2($fp)
        addiu   $Error, $fp, 2
        la      $4, string2_1
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
                
        li      $v0, 1
        syscall 
        la      $4, string2_2
        li      $v0, 5
        syscall 
        sw      $v0, LOCATION
        li      $Error, 1
        sw      $Error, 12($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $Error, 0($fp)
        lw      $Error, 2($fp)
        sle     $Error, $Error, $Error
        beq     $Error, $0, $L3
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $Error, 0($fp)
        addi    $Error, $Error, 1
                
        sw      $Error, 16($fp)
        lw      $4, 0($fp)
        jal     f
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 0($fp)
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
        lw      $fp, 20($sp)
        addiu   $sp, $sp, 24
        li      $v0, 10
        syscall 